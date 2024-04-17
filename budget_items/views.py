from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.db import models
from .models import BudgetItems


class BudgetItemsListView(ListView):
    model = BudgetItems
    template_name = "budget_items_list.html"

    def get_querysetView(self):
        return BudgetItems.objects.order_by("pk")[:50]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_budget'] = BudgetItems.objects.aggregate(total_budget=models.Sum('budget'))['total_budget']
        return context


class BudgetItemsDetailView(DetailView):
    model = BudgetItems
    template_name = "budget_items_detail.html"


class BudgetItemsCreateView(CreateView):
    model = BudgetItems
    fields = ["number", "cpc", "description", "budget", "budget_type", "bid"]
    template_name = "budget_items_create.html"
    success_url = reverse_lazy("budget_items:list")


class BudgetItemsDeleteView(DeleteView):
    model = BudgetItems
    success_url = reverse_lazy("budget_items:list")
    template_name = "budget_items_confirm_delete.html"


class BudgetItemsUpdateView(UpdateView):
    model = BudgetItems
    fields = ["number", "cpc", "description", "budget", "budget_type", "bid"]
    template_name = "budget_items_update.html"
    success_url = reverse_lazy("budget_items:list")
