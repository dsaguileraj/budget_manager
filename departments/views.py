from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Departments


class DepartmentsListView(ListView):
    model = Departments
    template_name = "departments_list.html"

    def get_queryset(self):
        return Departments.objects.order_by("name")[:50]


class DepartmentsDetailView(DetailView):
    model = Departments
    template_name = "departments_detail.html"


class DepartmentsCreateView(CreateView):
    model = Departments
    fields = ["name", "director"]
    template_name = "departments_create.html"
    success_url = reverse_lazy("departments:list")


class DepartmentsDeleteView(DeleteView):
    model = Departments
    success_url = reverse_lazy("departments:list")
    template_name = "departments_confirm_delete.html"


class DepartmentsUpdateView(UpdateView):
    model = Departments
    fields = ["name", "director"]
    template_name = "departments_update.html"
    success_url = reverse_lazy("departments:list")
