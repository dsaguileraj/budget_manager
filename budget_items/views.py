from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import BudgetItems


class BudgetItemsListView(ListView):
    model = BudgetItems
    template_name = "budget_items_list.html"

    def get_querysetView(self):
        return BudgetItems.objects.order_by("pk")[:50]


class BudgetItemsDetailView(DetailView):
    model = BudgetItems
    template_name = "budget_items_detail.html"


class BudgetItemsCreateView(CreateView):
    model = BudgetItems
    fields = "__all__"
    template_name = "budget_items_create.html"
    success_url = reverse_lazy("budget_items:list")


class BudgetItemsDeleteView(DeleteView):
    model = BudgetItems
    success_url = reverse_lazy("budget_items:list")


class BudgetItemsUpdateView(UpdateView):
    model = BudgetItems
    fields = "__all__"
    template_name = "budget_items_update.html"
    success_url = reverse_lazy("budget_items:list")
