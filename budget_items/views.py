from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import *


def index(request):
    return render(request, "index.html")


class BudgetItemsListView(generic.ListView):
    model = BudgetItems
    template_name = "budget_items.html"
    context_object_name = "budget_items_list"

    def get_queryset(self):
        return BudgetItems.objects.order_by("number")[:50]


class BudgetItemsDetalView(generic.DetailView):
    model = BudgetItems
    template_name = "detail_budget_item.html"


class BudgetItemsCreateView(generic.CreateView):
    model = BudgetItems
    fields = ["number", "cpc", "budget", "budget_type", "description", "bid"]
    template_name = "create_budget_item.html"
    success_url = reverse_lazy("budget_items")


class CertificationsListView(generic.ListView):
    model = Certifications
    template_name = "certifications.html"
    context_object_name = "certifications_list"

    def get_queryset(self):
        return Certifications.objects.order_by("number")[:50]


class CertificationsDetailView(generic.DetailView):
    model = Certifications
    template_name = "detail_certification.html"


class CertificationsCreateView(generic.CreateView):
    model = Certifications
    fields = ["number", "procedure", "budget_item",
              "department", "budget", "description", "period"]
    template_name = "create_certification.html"
    success_url = reverse_lazy("certifications")


class DepartmentsListView(generic.ListView):
    model = Departments
    template_name = "departments.html"
    context_object_name = "departments_list"

    def get_queryset(self):
        return Departments.objects.order_by("name")[:50]


class DepartmentsDetailView(generic.DetailView):
    model = Departments
    template_name = "detail_department.html"


class DepartmentsCreateView(generic.CreateView):
    model = Departments
    fields = ["name", "director"]
    template_name = "create_department.html"
    success_url = reverse_lazy("departments")


class ProceduresTypesListView(generic.ListView):
    model = ProceduresTypes
    template_name = "procedures_types.html"
    context_object_name = "procedures_types_list"

    def get_queryset(self):
        return ProceduresTypes.objects.order_by("name")[:50]


class ProceduresTypesDetailView(generic.DetailView):
    model = ProceduresTypes
    template_name = "detail_procedure_type"


class ProceduresTypesCreateView(generic.CreateView):
    model = ProceduresTypes
    fields = ["name", "regime", "product_type", "purchase_type"]
    template_name = "create_procedure_type.html"
    success_url = reverse_lazy("procedure_type")
