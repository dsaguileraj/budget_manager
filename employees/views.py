from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from .models import Employees


class EmployeesListView(ListView):
    model = Employees
    template_name = "employees_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Employees.objects.filter(
                models.Q(ci__icontains=query) | models.Q(name__icontains=query) | models.Q(
                    surname__icontains=query) | models.Q(email__icontains=query) | models.Q(user__icontains=query)
            ).order_by("number")
        else:
            return Employees.objects.order_by("ci")[:50]


class EmployeesDetailView(DetailView):
    model = Employees
    template_name = "employees_detail.html"


def create_employee(request):
    if request.method == "POST":
        ci = request.POST["ci"]
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        user = request.POST["user"]
        employee = Employees.objects.create(
            ci=ci,
            name=name,
            surname=surname,
            email=email,
            user=user
        )
        employee.save()
        return redirect(reverse_lazy(""))
    else:
        return render(request, "employees_create.html")


def delete_employee(request, pk):
    try:
        record = Employees.objects.get(pk=pk)
        record.delete()
        message = "Record deleted successfully"
    except Employees.DoesNotExist:
        message = "Record not found"
    if message == "Record deleted successfully":
        return redirect(reverse_lazy(""))
    else:
        return render(request, "employees_list.html", {"message": message})


def update_employee(request, pk):
    employee = Employees.objects.get(pk=pk)
    if request.method == "POST":
        employee.ci = request.POST["ci"]
        employee.name = request.POST["name"]
        employee.surname = request.POST["surname"]
        employee.email = request.POST["email"]
        employee.user = request.POST["user"]
        employee.save()
        return redirect(reverse_lazy(""))
    else:
        return render(request, "employees_update.html")
