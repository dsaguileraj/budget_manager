from django.db import models, IntegrityError
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Procedure, ProductType, PurchaseType, Regime


def list_procedure(request: HttpRequest) -> HttpResponse:
    object_list = Procedure.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    query = request.GET.get("q", "").strip()
    if query:
        result = Procedure.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(regime__icontains=query) |
            models.Q(product_type__icontains=query) |
            models.Q(purchase_type__icontains=query)
        ).order_by("name")
        if result:
            context["page_obj"] = result
        if not result:
            context["message"] = "No se encontraron coincidencias"
    return render(request, "procedure/list.html", context)


def detail_procedure(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        procedure = Procedure.objects.get(pk=pk)
    except Procedure.DoesNotExist:
        context = {"message": "Procedimiento no encontrado"}
        return render(request, "procedure/list.html", context)
    except ValueError:
        context = {"message": "ValueError"}
        return render(request, "procedure/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "procedure/list.html", context)
    else:
        context = {"procedure": procedure}
        return render(request, "procedure/detail.html", context)


def create_procedure(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {
        "regimes": Regime.choices,
        "product_types": ProductType.choices,
        "purchase_types": PurchaseType.choices,
    }
    if request.method == "POST":
        name = request.POST.get("name")
        regime = request.POST.get("regime")
        product_type = request.POST.get("product_type")
        purchase_type = request.POST.get("purchase_type")
        try:
            procedure = Procedure.objects.create(
                name=name.strip(),
                regime=regime,
                product_type=product_type,
                purchase_type=purchase_type
            )
        except IntegrityError as error:
            context["IntegrityError"] = error
            return render(request, "procedure/create.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "procedure/create.html", context)
        else:
            procedure.save()
            return redirect(reverse_lazy("procedure:list"))
    else:
        return render(request, "procedure/create.html", context)


def delete_procedure(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        procedure = Procedure.objects.get(pk=pk)
    except Procedure.DoesNotExist:
        context = {"message": "Procedimiento no encontrado"}
        return render(request, "procedure/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "procedure/list.html", context)
    try:
        procedure.delete()
    except models.ProtectedError as error:
        context = {"ProtectedError": error}
        return render(request, "procedure/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "procedure/list.html", context)
    else:
        return redirect(reverse_lazy("procedure:list"))


def update_procedure(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        procedure = Procedure.objects.get(pk=pk)
    except Procedure.DoesNotExist:
        context = {"message": "Procedimiento no encontrado"}
        return render(request, "procedure/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "procedure/list.html", context)
    else:
        context = {
            "regimes": Regime.choices,
            "product_types": ProductType.choices,
            "purchase_types": PurchaseType.choices,
            "procedure": procedure
        }
    if request.method == "POST":
        procedure.name = request.POST.get("name").strip()
        procedure.regime = request.POST.get("regime")
        procedure.product_type = request.POST.get("product_type")
        procedure.purchase_type = request.POST.get("purchase_type")
        try:
            procedure.save()
        except IntegrityError as error:
            context["IntegrityError"] = error
            return render(request, "procedure/update.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "procedure/update.html", context)
        else:
            return redirect(reverse_lazy("procedure:detail", args=[pk]))
    else:
        return render(request, "procedure/update.html", context)
