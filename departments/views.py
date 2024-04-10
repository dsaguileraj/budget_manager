from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Departments


class List(ListView):
    model = Departments
    template_name = "budget_items.html"
    context_object_name = "budget_items_list"

    def get_queryset(self):
        return Departments.objects.order_by("number")[:50]


class Detail(DetailView):
    model = Departments
    template_name = "detail_budget_item.html"


class Create(CreateView):
    model = Departments
    fields = ["number", "cpc", "budget", "budget_type", "description", "bid"]
    template_name = "create_budget_item.html"
    success_url = reverse_lazy("budget_items")


class Delete(DeleteView):
    model = Departments
    success_url = reverse_lazy("budget_items")


class Update(UpdateView):
    pass
