from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import ProceduresTypes


class List(ListView):
    model = ProceduresTypes
    template_name = "budget_items.html"
    context_object_name = "budget_items_list"

    def get_queryset(self):
        return ProceduresTypes.objects.order_by("number")[:50]


class Detail(DetailView):
    model = ProceduresTypes
    template_name = "detail_budget_item.html"


class Create(CreateView):
    model = ProceduresTypes
    fields = ["number", "cpc", "budget", "budget_type", "description", "bid"]
    template_name = "create_budget_item.html"
    success_url = reverse_lazy("budget_items")


class Delete(DeleteView):
    model = ProceduresTypes
    success_url = reverse_lazy("budget_items")


class Update(UpdateView):
    pass
