from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import ProceduresTypes


class ProceduresTypesListView(ListView):
    model = ProceduresTypes
    template_name = "procedures_types_list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return ProceduresTypes.objects.filter(
                models.Q(name__icontains = query) |  models.Q(regime__icontains = query)  |  models.Q(product_type__icontains = query) |  models.Q(purchase_type__icontains = query)
            ).order_by("name")
        else:
            return ProceduresTypes.objects.order_by("name")[:50]


class ProceduresTypesDetailView(DetailView):
    model = ProceduresTypes
    template_name = "procedures_types_detail.html"


class ProceduresTypesCreateView(CreateView):
    model = ProceduresTypes
    fields = ["name", "regime", "product_type", "purchase_type"]
    template_name = "procedures_types_create.html"
    success_url = reverse_lazy("procedures_types:list")


def delete_procedure_type(request, pk):
    try:
        record = ProceduresTypes.objects.get(pk=pk)
        record.delete()
        message = "Record deleted successfully"
    except ProceduresTypes.DoesNotExist:
        message = "Record not found"
    if message == "Record deleted successfully":
        return redirect(reverse_lazy("procedures_types:list"))
    else:
        return render(request, "procedures_types_list.html", {"message": message})


class ProceduresTypesUpdateView(UpdateView):
    model = ProceduresTypes
    fields = ["name", "regime", "product_type", "purchase_type"]
    template_name = "procedures_types_update.html"
    success_url = reverse_lazy("procedures_types:list")
