from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Certifications


class List(ListView):
    model = Certifications
    template_name = "list.html"

    def get_queryset(self):
        return Certifications.objects.order_by("pk")[:50]


class Detail(DetailView):
    model = Certifications
    template_name = "detail.html"


class Create(CreateView):
    model = Certifications
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("certifications:list")


class Delete(DeleteView):
    model = Certifications
    success_url = reverse_lazy("certifications:list")


class Update(UpdateView):
    model = Certifications
    fields = "__all__"
    template_name = "update.html"
    success_url = reverse_lazy("certifications:list")
