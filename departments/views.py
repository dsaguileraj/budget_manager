from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Departments


class DepartmentsListView(ListView):
    model = Departments
    template_name = "departments_list.html"
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Departments.objects.filter(
                models.Q(name__icontains = query) |  models.Q(director__icontains = query)
            ).order_by("name")
        else:
            return Departments.objects.order_by("name")[:50]


class DepartmentsDetailView(DetailView):
    model = Departments
    template_name = "departments_detail.html"


class DepartmentsCreateView(CreateView):
    model = Departments
    fields = ["name", "director"]
    template_name = "departments_create.html"
    success_url = reverse_lazy("departments:list")


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


class DepartmentsUpdateView(UpdateView):
    model = Departments
    fields = ["name", "director"]
    template_name = "departments_update.html"
    success_url = reverse_lazy("departments:list")
