from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, render
from django.db import models
from .models import BudgetItems
import pandas


class BudgetItemsListView(ListView):
    model = BudgetItems
    template_name = "budget_items/list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return BudgetItems.objects.filter(
                models.Q(number__icontains=query) | models.Q(cpc__icontains=query) | models.Q(
                    description__icontains=query) | models.Q(activity__icontains=query) | models.Q(budget__icontains=query)
            ).order_by("number")
        else:
            return BudgetItems.objects.order_by("number")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_budget"] = BudgetItems.objects.aggregate(
            total_budget=models.Sum("budget"))["total_budget"]
        return context


class BudgetItemsDetailView(DetailView):
    model = BudgetItems
    template_name = "budget_items/detail.html"


def create_budget_item(request):
    if request.method == "POST":
        number = request.POST["number"]
        cpc = request.POST["cpc"]
        budget = request.POST["budget"]
        budget_type = request.POST["budget_type"]
        description = request.POST["description"]
        activity = request.POST["activity"]
        bid = request.POST.get("bid") == "on"
        budget_item = BudgetItems.objects.create(
            number=number,
            cpc=cpc,
            budget=budget,
            budget_type=budget_type,
            description=description,
            activity=activity,
            bid=bid
        )
        budget_item.save()
        return redirect(reverse_lazy("budget_items:list"))
    else:
        return render(request, "budget_items/create.html")


def delete_budget_item(request, pk):
    try:
        budget_item = BudgetItems.objects.get(pk=pk)
        budget_item.delete()
        deleted = True
    except BudgetItems.DoesNotExist:
        deleted = False
    if deleted:
        return redirect(reverse_lazy("budget_items:list"))
    else:
        return render(request, "budget_items/list.html")


def update_budget_item(request, pk):
    budget_item = BudgetItems.objects.get(pk=pk)
    if request.method == "POST":
        budget_item.number = request.POST["number"]
        budget_item.cpc = request.POST["cpc"]
        budget_item.budget = request.POST["budget"]
        budget_item.budget_type = request.POST["budget_type"]
        budget_item.description = request.POST["description"]
        budget_item.activity = request.POST["activity"]
        budget_item.bid = request.POST.get("bid") == "on"
        budget_item.save()
        return redirect(reverse_lazy("budget_items:list"))
    else:
        return render(request, "budget_items/update.html", {"budget_item": budget_item})


def upload_file(request):
    if request.method == "POST":
        file = request.FILES["file"]
        data = pandas.read_excel(file, engine="openpyxl")
        for index, row in data.iterrows():
            BudgetItems.objects.create(
                number=row["Número"],
                cpc=row["CPC"],
                budget=row["Presupuesto"],
                budget_type=row["Tipo de Presupuesto"],
                description=row["Descripción"],
                activity=row["Actividad"],
                bid=row["BID"]
            )
        return redirect(reverse_lazy("budget_items:list"))
    return render(request, "budget_items/create_excel.html")