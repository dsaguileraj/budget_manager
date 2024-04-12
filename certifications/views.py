from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Certifications


class CertificationsListView(ListView):
    model = Certifications
    template_name = "certifications_list.html"

    def get_queryset(self):
        return Certifications.objects.order_by("pk")[:50]


class CertificationsDetailView(DetailView):
    model = Certifications
    template_name = "certifications_detail.html"


class CertificationsCreateView(CreateView):
    model = Certifications
    fields = "__all__"
    template_name = "certifications_create.html"
    success_url = reverse_lazy("certifications:list")


class CertificationsDeleteView(DeleteView):
    model = Certifications
    success_url = reverse_lazy("certifications:list")


class CertificationsUpdateView(UpdateView):
    model = Certifications
    fields = "__all__"
    template_name = "certifications_update.html"
    success_url = reverse_lazy("certifications:list")
