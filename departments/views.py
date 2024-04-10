from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Departments


class List(ListView):
    model = Departments
    template_name = "list.html"

    def get_queryset(self):
        return Departments.objects.order_by("pk")[:50]


class Detail(DetailView):
    model = Departments
    template_name = "detail.html"


class Create(CreateView):
    model = Departments
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("departments:list")


class Delete(DeleteView):
    model = Departments
    success_url = reverse_lazy("departments:list")


class Update(UpdateView):
    model = Departments
    fields = "__all__"
    template_name = "update.html"
    success_url = reverse_lazy("departments:list")
