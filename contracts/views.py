from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from .models import Contracts, Certifications, Employees


class ContractsListView(ListView):
    model = Contracts
    template_name = "contracts/list.html"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Contracts.objects.filter(
                models.Q(id__icontains=query) | models.Q(certification__icontains=query) | models.Q(
                    admin__icontains=query) | models.Q(contractor__icontains=query)
            ).order_by("id")
        else:
            return Contracts.objects.order_by("id")


class ContractsDetailView(DetailView):
    model = Contracts
    template_name = "contracts/detail.html"


def create_contract(request):
    context = {
        "employees": Employees.objects.all(),
        "certifications": Certifications.objects.all()
    }
    if request.method == "POST":
        id = request.POST["id"]
        certification_id = request.POST["certification"]
        advance = request.POST.get("advance") == "on"
        admin_id = request.POST["admin"]
        contractor = request.POST["contractor"]
        date = request.POST["date"]
        duration = request.POST["duration"]
        certification = Certifications.objects.get(pk=certification_id)
        admin = Employees.objects.get(pk=admin_id)
        contract = Contracts.objects.create(
            id=id,
            certification=certification,
            advance=advance,
            admin=admin,
            contractor=contractor,
            date=date,
            duration=duration
        )
        contract.save()
        return redirect(reverse_lazy("contracts:list"))
    else:
        return render(request, "contracts/create.html", context)


def delete_contract(request, pk):
    try:
        contract = Contracts.objects.get(pk=pk)
        contract.delete()
        deleted = True
    except Contracts.DoesNotExist:
        deleted = False
    if deleted:
        return redirect(reverse_lazy("contracts:list"))
    else:
        return render(request, "contracts/list.html")


def update_contract(request, pk):
    contract = Contracts.objects.get(pk=pk)
    context = {
        "employees": Employees.objects.all(),
        "certifications": Certifications.objects.all(),
        "contract": contract
    }
    if request.method == "POST":
        admin_id = request.POST["admin"]
        certification_id = request.POST["certification"]
        contract.id = request.POST["id"]
        contract.advance = request.POST.get("advance") == "on"
        contract.contractor = request.POST["contractor"]
        contract.date = request.POST["date"]
        contract.duration = request.POST["duration"]
        contract.certification = Certifications.objects.get(
            pk=certification_id)
        contract.admin = Employees.objects.get(pk=admin_id)
        contract.save()
        return redirect(reverse_lazy("contracts:list"))
    else:
        return render(request, "contracts/update.html", context)
