from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView
from django.core.validators import ValidationError
# from .forms import CertificationsForm
from .models import Certifications
from budget_items.models import *
from departments.models import *
from procedures_types.models import *

class CertificationsListView(ListView):
    model = Certifications
    template_name = "certifications_list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Certifications.objects.filter(
                models.Q(number__icontains = query) |  models.Q(budget_item__icontains = query) |  models.Q(description__icontains = query) |  models.Q(activity__icontains = query)
            ).order_by("number")
        else:
            return Certifications.objects.order_by("number")[:50]


class CertificationsDetailView(DetailView):
    model = Certifications
    template_name = "certifications_detail.html"



def create_certification(request):
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
        
        # try:
        #     procedure = ProceduresTypes.objects.get(pk=procedure_id)
        #     budget_item = BudgetItems.objects.get(pk=budget_item_id)
        #     department = Departments.objects.get(pk=department_id)
        # except ProceduresTypes.DoesNotExist:
        #     return render(request, "certifications/certifications_form.html", {"error": "Invalid procedure"})
        # except BudgetItems.DoesNotExist:
        #     return render(request, "certifications/certifications_form.html", {"error": "Invalid budget item"})
        # except Departments.DoesNotExist:
        #     return render(request, "certifications/certifications_form.html", {"error": "Invalid department"})

        certification = Certifications.objects.create(
            procedure=procedure,
            budget_item=budget_item,
            department=department,
            budget=budget,
            description=description,
            period=period
        )
        total_certifications_budget = Certifications.objects.filter(budget_item=budget_item).aggregate(models.Sum("budget"))["budget__sum"] or 0
        if total_certifications_budget + certification.budget <= budget_item.budget:
            certification.save()
            return redirect(reverse_lazy("certifications:list"))
        else:
            raise ValidationError("Total budget for certifications exceeds budget item limit")
    else:
        procedures = ProceduresTypes.objects.all()
        budget_items = BudgetItems.objects.all()
        departments = Departments.objects.all()

        context = {
            "procedures": procedures,
            "budget_items": budget_items,
            "departments": departments,
        }

        return render(request, "certifications_create.html", context)


# def create_certification(request):
#     if request.method == "POST":
#         try:
#             form = CertificationsForm(request.POST)
#             if form.is_valid():
#                 certification = form.save(commit=False)
#                 budget_item = certification.budget_item
#                 total_certifications_budget = Certifications.objects.filter(budget_item=budget_item).aggregate(models.Sum("budget"))["budget__sum"] or 0

#                 if total_certifications_budget + certification.budget <= budget_item.budget:
#                     certification.save()
#                     return redirect(reverse_lazy("certifications:list"))
#                 else:
#                     raise ValidationError("Total budget for certifications exceeds budget item limit")
#         except(ValidationError, Exception) as error:
#             return render(
#                 request,
#                 "certifications_create.html",
#                 {
#                     "form": form,
#                     "error_message": str(error)
#                 }
#             )
#     else:
#         form = CertificationsForm()
#     context = {"form": form}
#     return render(request, "certifications_create.html", context)


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
        return render(request, "certifications_list.html", {"message": message})


class CertificationsUpdateView(UpdateView):
    model = Certifications
    fields = ["budget_item", "description", "department", "budget", "procedure", "period"]
    template_name = "certifications_update.html"
    success_url = reverse_lazy("certifications:list")
