from datetime import datetime
from django.db import IntegrityError, models
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Contract, Certification, Employee


def list_contract(request: HttpRequest) -> HttpResponse:
    object_list = Contract.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    query = request.GET.get("q", "").strip()
    if query:
        result = Contract.objects.filter(
            models.Q(number__icontains=query) |
            models.Q(certification__description__icontains=query) |
            models.Q(certification__budget__icontains=query) |
            models.Q(admin__first_name__icontains=query) |
            models.Q(admin__middle_name__icontains=query) |
            models.Q(admin__first_last_name__icontains=query) |
            models.Q(admin__middle_last_name__icontains=query) |
            models.Q(contractor__icontains=query)
        ).order_by("number")
        if result:
            context["page_obj"] = result
        if not result:
            context["message"] = "No se encontraron coincidencias"
    return render(request, "contract/list.html", context)


def detail_contract(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        context = {"message": error}
        return render(request, "contract/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "contract/list.html", context)
    else:
        context = {"contract": contract}
        return render(request, "contract/detail.html", context)


def create_contract(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {
        "employees": Employee.objects.all(),
        "certifications": Certification.objects.all(),
    }
    if request.method == "POST":
        number = request.POST.get("number")
        contractor = request.POST.get("contractor")
        suscription_str = request.POST.get("suscription")
        duration = request.POST.get("duration")
        description = request.POST.get("description")
        selected_certifications = request.POST.getlist("certification")
        certs = Certification.objects.filter(
            pk__in=selected_certifications)
        try:
            admin = Employee.objects.get(pk=request.POST.get("admin"))
        except Employee.DoesNotExist:
            context["message"] = "El administrador seleccionado no existente"
            return render(request, "contract/create.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "contract/create.html", context)
        try:
            new_contract = Contract.objects.create(
                number=number.strip(),
                admin=admin,
                contractor=contractor.strip(),
                description=description.strip(),
                suscription=datetime.strptime(
                    suscription_str, "%Y-%m-%d").date(),
                duration=duration,
            )
        except IntegrityError as error:
            context["IntegrityError"] = error
            return render(request, "contract/create.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "contract/create.html", context)
        else:
            new_contract.certification.add(*certs)
            return redirect(reverse_lazy("contract:list"))
    else:
        return render(request, "contract/create.html", context)


def delete_contract(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        context = {"message": "Contrato no encontrado"}
        return render(request, "contract/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "contract/list.html", context)
    try:
        contract.delete()
    except models.ProtectedError as error:
        context = {"ProtectedError": error}
        return render(request, "contract/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "contract/list.html", context)
    else:
        return redirect(reverse_lazy("contract:list"))


def update_contract(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        context = {"message": "Contrato no encontrado"}
        return render(request, "contract/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "contract/list.html", context)
    else:
        context = {
            "contract": contract,
            "employees": Employee.objects.all(),
            "certifications": Certification.objects.all(),
            "date": str(contract.suscription),
        }
    if request.method == "POST":
        number = request.POST.get("number")
        contractor = request.POST.get("contractor")
        suscription_str = request.POST.get("suscription")
        duration = request.POST.get("duration")
        description = request.POST.get("description")
        selected_certifications = request.POST.getlist("certification")
        try:
            admin = Employee.objects.get(pk=request.POST.get("admin"))
        except Employee.DoesNotExist:
            context["message"] = "Administrador seleccionado no existente"
            return render(request, "contract/update.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "contract/update.html", context)
        else:
            contract.number = number.strip()
            contract.contractor = contractor.strip()
            contract.suscription = datetime.strptime(
                suscription_str, "%Y-%m-%d").date()
            contract.duration = duration
            contract.description = description.strip()
            contract.admin = admin
            contract.certification.clear()
            certs = Certification.objects.filter(
                pk__in=selected_certifications)
            contract.certification.add(*certs)
        try:
            contract.save()
        except IntegrityError as error:
            context["IntegrityError"] = error
            return render(request, "contract/update.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "contract/update.html", context)
        else:
            return redirect(reverse_lazy("contract:detail", args=[pk]))
    else:
        return render(request, "contract/update.html", context)
