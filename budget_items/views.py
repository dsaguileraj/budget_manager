from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import BudgetItems


class List(ListView):
    model = BudgetItems
    template_name = "list.html"

    def get_queryset(self):
        return BudgetItems.objects.order_by("pk")[:50]


class Detail(DetailView):
    model = BudgetItems
    template_name = "detail.html"


class Create(CreateView):
    model = BudgetItems
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("budget_items:list")


class Delete(DeleteView):
    model = BudgetItems
    success_url = reverse_lazy("budget_items:list")


class Update(UpdateView):
    model = BudgetItems
    fields = "__all__"
    template_name = "update.html"
    success_url = reverse_lazy("budget_items:list")
