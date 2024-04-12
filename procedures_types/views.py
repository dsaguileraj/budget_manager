from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import ProceduresTypes


class ProceduresTypesListView(ListView):
    model = ProceduresTypes
    template_name = "procedures_types_list.html"

    def get_queryset(self):
        return ProceduresTypes.objects.order_by("pk")[:50]


class ProceduresTypesDetailView(DetailView):
    model = ProceduresTypes
    template_name = "procedures_types_detail.html"


class ProceduresTypesCreateView(CreateView):
    model = ProceduresTypes
    fields = "__all__"
    template_name = "procedures_types_create.html"
    success_url = reverse_lazy("procedures_types:list")


class ProceduresTypesDeleteView(DeleteView):
    model = ProceduresTypes
    success_url = reverse_lazy("procedures_types:list")


class ProceduresTypesUpdateView(UpdateView):
    model = ProceduresTypes
    fields = "__all__"
    template_name = "procedures_types_update.html"
    success_url = reverse_lazy("procedures_types:list")
