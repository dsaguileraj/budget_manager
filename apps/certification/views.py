from decimal import Decimal
from django.core.paginator import Paginator
from django.db import IntegrityError, models
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import BudgetItem, Certification, Department, Procedure


def list_certification(request: HttpRequest) -> HttpResponse:
    object_list = Certification.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    query = request.GET.get("q", "").strip()
    if query:
        result = Certification.objects.filter(
            models.Q(number__icontains=query) |
            models.Q(budget_item__number__icontains=query) |
            models.Q(description__icontains=query) |
            models.Q(budget_item__activity__icontains=query) |
            models.Q(budget__icontains=query)
        ).order_by("number")
        if result:
            context["page_obj"] = result
        if not result:
            context["message"] = "No se encontraron coincidencias"
    return render(request, "certification/list.html", context)


def detail_certification(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        certification = Certification.objects.get(pk=pk)
    except Certification.DoesNotExist:
        context = {"message": "Certificación no encontrada"}
        return render(request, "certification/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "certification/list.html", context)
    else:
        context = {"certification": certification}
        return render(request, "certification/detail.html", context)


def create_certification(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {
        "procedures": Procedure.objects.all(),
        "budget_items": BudgetItem.objects.all(),
        "departments": Department.objects.all()
    }
    if request.method == "POST":
        number = request.POST.get("number")
        budget = Decimal(request.POST.get("budget"))
        description = request.POST.get("description")
        try:
            budget_item = BudgetItem.objects.get(
                pk=request.POST.get("budget_item"))
        except BudgetItem.DoesNotExist:
            context["message"] = "Partida seleccionada no existente"
            return render(request, "certificaion/create.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "certification/create.html", context)
        else:
            total_certification_budget = Certification.objects.filter(
                budget_item=budget_item).aggregate(models.Sum("budget"))["budget__sum"] or 0
        try:
            department = Department.objects.get(
                pk=request.POST.get("department"))
        except Department.DoesNotExist:
            context["message"] = "Departamento seleccionado no existente"
            return render(request, "certificaion/create.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "certification/create.html", context)
        try:
            procedure = Procedure.objects.get(pk=request.POST.get("procedure"))
        except Procedure.DoesNotExist:
            context["message"] = "Procedimiento seleccionado no existente"
            return render(request, "certificaion/create.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "certification/create.html", context)
        if total_certification_budget + budget <= budget_item.budget:
            try:
                certification = Certification.objects.create(
                    number=number.strip(),
                    procedure=procedure,
                    budget_item=budget_item,
                    department=department,
                    budget=budget,
                    description=description.strip(),
                )
            except IntegrityError as error:
                context["IntegrityError"] = error
                return render(request, "certification/create.html", context)
            except Exception as error:
                context["Exception"] = error
                return render(request, "certification/create.html", context)
            else:
                certification.save()
                return redirect(reverse_lazy("certification:list"))
        else:
            context["message"] = "El presupuesto a certificar excede el saldo disponible de la partida"
            return render(request, "certification/create.html", context)
    else:
        return render(request, "certification/create.html", context)


def delete_certification(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        certification = Certification.objects.get(pk=pk)
    except Certification.DoesNotExist:
        context = {"message": "Certificación no encontrada"}
        return render(request, "certification/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "certification/list.html", context)
    try:
        certification.delete()
    except models.ProtectedError as error:
        context = {"ProtectedError": error}
        return render(request, "certification/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "certification/list.html", context)
    else:
        return redirect(reverse_lazy("certification:list"))


def update_certification(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        certification = Certification.objects.get(pk=pk)
    except Certification.DoesNotExist:
        context = {"message": "Certificación no encontrada"}
        return render(request, "certification/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "certification/list.html", context)
    else:
        context = {
            "procedures": Procedure.objects.all(),
            "budget_items": BudgetItem.objects.all(),
            "departments": Department.objects.all(),
            "certification": certification,
        }
    if request.method == "POST":
        certification.number = request.POST.get("number").strip()
        certification.budget = Decimal(request.POST.get("budget"))
        certification.description = request.POST.get("description").strip()
        try:
            certification.budget_item = BudgetItem.objects.get(
                pk=request.POST.get("budget_item"))
        except BudgetItem.DoesNotExist:
            context["message"] = "Partida seleccionada no existente"
            return render(request, "certificaion/update.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "certification/update.html", context)
        else:
            total_certification_budget = Certification.objects.filter(
                budget_item=certification.budget_item).aggregate(models.Sum("budget"))["budget__sum"] or 0
        try:
            certification.department = Department.objects.get(
                pk=request.POST.get("department"))
        except Department.DoesNotExist:
            context["message"] = "Departamento seleccionado no existente"
            return render(request, "certificaion/update.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "certification/update.html", context)
        try:
            certification.procedure = Procedure.objects.get(
                pk=request.POST.get("procedure"))
        except Procedure.DoesNotExist:
            context["message"] = "Procedimiento seleccionado no existente"
            return render(request, "certificaion/update.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "certification/update.html", context)
        if total_certification_budget + certification.budget <= certification.budget_item.budget:
            try:
                certification.save()
            except IntegrityError as error:
                context["IntegrityError"] = error
                return render(request, "certification/update.html", context)
            except Exception as error:
                context["Exception"] = error
                return render(request, "certification/update.html", context)
            else:
                return redirect(reverse_lazy("certification:detail", args=[pk]))
        else:
            context["message"] = "El presupuesto a certificar excede el saldo disponible de la partida"
            return render(request, "certification/update.html", context)
    else:
        return render(request, "certification/update.html", context)
