from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import BudgetItems, Certifications, Departments, ProceduresTypes


class CertificationsListView(ListView):
    model = Certifications
    template_name = "certifications/list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Certifications.objects.filter(
                models.Q(number__icontains=query) | models.Q(
                    description__icontains=query)
            ).order_by("number")
        else:
            return Certifications.objects.order_by("number")[:50]


class CertificationsDetailView(DetailView):
    model = Certifications
    template_name = "certifications/detail.html"


def create_certification(request):
    context = {
        "procedures": ProceduresTypes.objects.all(),
        "budget_items": BudgetItems.objects.all(),
        "departments": Departments.objects.all()
    }
    if request.method == "POST":
        procedure_id = request.POST["procedure"]
        budget_item_id = request.POST["budget_item"]
        department_id = request.POST["department"]
        budget = float(request.POST["budget"])
        description = request.POST["description"]
        period = int(request.POST["period"])
        procedure = ProceduresTypes.objects.get(pk=procedure_id)
        budget_item = BudgetItems.objects.get(pk=budget_item_id)
        department = Departments.objects.get(pk=department_id)
        total_certifications_budget = Certifications.objects.filter(
            budget_item=budget_item).aggregate(models.Sum("budget"))["budget__sum"] or 0
        if total_certifications_budget + budget <= budget_item.budget:
            certification = Certifications.objects.create(
                procedure=procedure,
                budget_item=budget_item,
                department=department,
                budget=budget,
                description=description,
                period=period
            )
            certification.save()
            return redirect(reverse_lazy("certifications:list"))
        else:
            context["message"] = "Total budget for certifications exceeds budget item limit"
            return render(request, "certifications/create.html", context)
    else:
        return render(request, "certifications/create.html", context)


def delete_certification(request, pk):
    try:
        record = Certifications.objects.get(pk=pk)
        record.delete()
        message = "Record deleted successfully"
    except Certifications.DoesNotExist:
        message = "Record not found"
    if message == "Record deleted successfully":
        return redirect(reverse_lazy("certifications:list"))
    else:
        return render(request, "certifications/list.html", {"message": message})


def update_certification(request, pk):
    certification = Certifications.objects.get(pk=pk)
    context = {
        "procedures": ProceduresTypes.objects.all(),
        "budget_items": BudgetItems.objects.all(),
        "departments": Departments.objects.all()
    }
    if request.method == "POST":
        procedure_id = request.POST["procedure"]
        budget_item_id = request.POST["budget_item"]
        department_id = request.POST["department"]
        certification.budget = request.POST["budget"]
        certification.description = request.POST["description"]
        certification.period = request.POST["period"]
        certification.procedure = ProceduresTypes.objects.get(pk=procedure_id)
        certification.budget_item = BudgetItems.objects.get(pk=budget_item_id)
        certification.department = Departments.objects.get(pk=department_id)
        certification.save()
        return redirect(reverse_lazy("certifications:list"))
    else:
        return render(request, "certifications/update.html", context)
