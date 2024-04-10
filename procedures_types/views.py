from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import ProceduresTypes


class List(ListView):
    model = ProceduresTypes
    template_name = "list.html"

    def get_queryset(self):
        return ProceduresTypes.objects.order_by("pk")[:50]


class Detail(DetailView):
    model = ProceduresTypes
    template_name = "detail.html"


class Create(CreateView):
    model = ProceduresTypes
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("procedures_types:list")


class Delete(DeleteView):
    model = ProceduresTypes
    success_url = reverse_lazy("procedures_types:list")


class Update(UpdateView):
    model = ProceduresTypes
    fields = "__all__"
    template_name = "update.html"
    success_url = reverse_lazy("procedures_types:list")
