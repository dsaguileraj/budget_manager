from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from .models import Departments, Employees


class DepartmentsListView(ListView):
    model = Departments
    template_name = "departments/list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Departments.objects.filter(
                models.Q(name__icontains=query) | models.Q(director__name__icontains=query) | models.Q(
                    director__surname__icontains=query) | models.Q(director__ci__icontains=query)
            ).order_by("name")
        else:
            return Departments.objects.order_by("name")


class DepartmentsDetailView(DetailView):
    model = Departments
    template_name = "departments/detail.html"


def create_department(request):
    if request.method == "POST":
        name = request.POST["name"]
        director = Employees.objects.get(pk=request.POST["director"])
        department = Departments.objects.create(
            name=name,
            director=director
        )
        department.save()
        return redirect(reverse_lazy("departments:list"))
    else:
        return render(request, "departments/create.html", {"employees": Employees.objects.all()})


def delete_department(request, pk):
    try:
        department = Departments.objects.get(pk=pk)
        department.delete()
        deleted = True
    except Departments.DoesNotExist:
        deleted = False
    if deleted:
        return redirect(reverse_lazy("departments:list"))
    else:
        return render(request, "departments/list.html")


def update_department(request, pk):
    department = Departments.objects.get(pk=pk)
    if request.method == "POST":
        department.name = request.POST["name"]
        department.director = request.POST["director"]
        department.save()
        return redirect(reverse_lazy("departments:list"))
    else:
        return render(request, "departments/update.html", {"department": department})
