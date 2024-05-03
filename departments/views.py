from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from .models import Departments, Employees


class DepartmentsListView(ListView):
    model = Departments
    template_name = "departments_list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Departments.objects.filter(
                models.Q(name__icontains=query) | models.Q(
                    director__icontains=query)
            ).order_by("name")
        else:
            return Departments.objects.order_by("name")[:50]


class DepartmentsDetailView(DetailView):
    model = Departments
    template_name = "departments_detail.html"


def create_department(request):
    if request.method == "POST":
        name = request.POST["name"]
        director = request.POST["director"]
        department = Departments.objects.create(
            name=name,
            director=director
        )
        department.save()
        return redirect(reverse_lazy("departments:list"))
    else:
        return render(request, "departments_create.html")


def delete_department(request, pk):
    try:
        record = Departments.objects.get(pk=pk)
        record.delete()
        message = "Record deleted successfully"
    except Departments.DoesNotExist:
        message = "Record not found"
    if message == "Record deleted successfully":
        return redirect(reverse_lazy("departments:list"))
    else:
        return render(request, "departments_list.html", {"message": message})


def update_department(request, pk):
    department = Departments.objects.get(pk=pk)
    if request.method == "POST":
        department.name = request.POST["name"]
        department.director = request.POST["director"]
        department.save()
        return redirect(reverse_lazy("departments:list"))
    else:
        return render(request, "departments_update.html", {"department": department})


class EmployeesListView(ListView):
    model = Employees
    template_name = "employees_list.html"


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
