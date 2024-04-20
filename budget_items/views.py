from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.db import models
from .models import BudgetItems


class BudgetItemsListView(ListView):
    model = BudgetItems
    template_name = "budget_items_list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return BudgetItems.objects.filter(
                models.Q(number__icontains = query) |  models.Q(cpc__icontains = query)
            ).order_by("number")
        else:
            return BudgetItems.objects.order_by("number")[:50]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_budget"] = BudgetItems.objects.aggregate(total_budget = models.Sum("budget"))["total_budget"]
        return context


class BudgetItemsDetailView(DetailView):
    model = BudgetItems
    template_name = "budget_items_detail.html"


class BudgetItemsCreateView(CreateView):
    model = BudgetItems
    fields = ["number", "cpc", "description", "budget", "budget_type", "activity", "bid"]
    template_name = "budget_items_create.html"
    success_url = reverse_lazy("budget_items:list")


class BudgetItemsDeleteView(DeleteView):
    model = BudgetItems
    success_url = reverse_lazy("budget_items:list")
    template_name = "budget_items_confirm_delete.html"


class BudgetItemsUpdateView(UpdateView):
    model = BudgetItems
    fields = ["number", "cpc", "description", "budget", "budget_type", "activity", "bid"]
    template_name = "budget_items_update.html"
    success_url = reverse_lazy("budget_items:list")
