from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from .models import *


class ProceduresTypesListView(ListView):
    model = ProceduresTypes
    template_name = "procedures_types/list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return ProceduresTypes.objects.filter(
                models.Q(name__icontains=query) | models.Q(regime__icontains=query) | models.Q(
                    product_type__icontains=query) | models.Q(purchase_type__icontains=query)
            ).order_by("name")
        else:
            return ProceduresTypes.objects.order_by("name")


class ProceduresTypesDetailView(DetailView):
    model = ProceduresTypes
    template_name = "procedures_types/detail.html"


def create_procedure_type(request):
    context = {
        "regime_choices": REGIME_CHOICES,
        "product_type_choices": PRODUCT_TYPE_CHOICES,
        "purchase_type_choices": PURCHASE_TYPE_CHOICES,
    }
    if request.method == "POST":
        name = request.POST["name"]
        regime = request.POST["regime"]
        product_type = request.POST["product_type"]
        purchase_type = request.POST["purchase_type"]
        procedure_type = ProceduresTypes.objects.create(
            name=name,
            regime=regime,
            product_type=product_type,
            purchase_type=purchase_type
        )
        procedure_type.save()
        return redirect(reverse_lazy("procedures_types:list"))
    else:
        return render(request, "procedures_types/create.html", context)


def delete_procedure_type(request, pk):
    try:
        procedure = ProceduresTypes.objects.get(pk=pk)
        procedure.delete()
        deleted = True
    except ProceduresTypes.DoesNotExist:
        deleted = False
    if deleted:
        return redirect(reverse_lazy("procedures_types:list"))
    else:
        return render(request, "procedures_types/list.html")


def update_procedure_type(request, pk):
    procedure_type = ProceduresTypes.objects.get(pk=pk)
    context = {
        "regime_choices": REGIME_CHOICES,
        "product_type_choices": PRODUCT_TYPE_CHOICES,
        "purchase_type_choices": PURCHASE_TYPE_CHOICES,
        "procedure_type": procedure_type
    }
    if request.method == "POST":
        procedure_type.name = request.POST["name"]
        procedure_type.regime = request.POST["regime"]
        procedure_type.product_type = request.POST["product_type"]
        procedure_type.purchase_type = request.POST["purchase_type"]
        procedure_type.save()
        return redirect(reverse_lazy("procedures_types:list"))
    else:
        return render(request, "procedures_types/update.html", context)
