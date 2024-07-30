from django.db import models
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Contract, Certification, Employee


def list_contract(request: HttpRequest) -> HttpResponse:
    object_list = Contract.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': object_list,
        'page_obj': page_obj,
    }
    query = request.GET.get('q', '')
    if query:
        result = Contract.objects.filter(
            models.Q(id__icontains=query) |
            models.Q(certification__description__icontains=query) |
            models.Q(certification__budget__icontains=query) |
            models.Q(admin__name__icontains=query) |
            models.Q(admin__surname__icontains=query) |
            models.Q(contractor__icontains=query)
        ).order_by('id')
        if result:
            context['object_list'] = result
        if not result:
            context['query_message'] = 'No se encontraron coincidencias'
    return render(request, 'contract/list.html', context)


class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contract/detail.html'


def create_contract(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {
        'employee': Employee.objects.all(),
        'certification': Certification.objects.all()
    }
    if request.method == 'POST':
        id = request.POST['id']
        certification_id = request.POST['certification']
        admin_id = request.POST['admin']
        contractor = request.POST['contractor']
        date = request.POST['date']
        duration = request.POST['duration']
        certification = Certification.objects.get(pk=certification_id)
        admin = Employee.objects.get(pk=admin_id)
        contract = Contract.objects.create(
            id=id,
            certification=certification,
            admin=admin,
            contractor=contractor,
            date=date,
            duration=duration
        )
        contract.save()
        return redirect(reverse_lazy('contract:list'))
    else:
        return render(request, 'contract/create.html', context)


def delete_contract(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        contract = Contract.objects.get(pk=pk)
        contract.delete()
        deleted = True
    except Contract.DoesNotExist:
        deleted = False
    except models.ProtectedError:
        return redirect(reverse_lazy('authentication:error'))
    if deleted:
        return redirect(reverse_lazy('contract:list'))
    else:
        return render(request, 'contract/list.html')


def update_contract(request, pk):
    contract = Contract.objects.get(pk=pk)
    context = {
        'employee': Employee.objects.all(),
        'certification': Certification.objects.all(),
        'contract': contract
    }
    if request.method == 'POST':
        admin_id = request.POST['admin']
        certification_id = request.POST['certification']
        contract.pk = request.POST['id']
        contract.advance = request.POST.get('advance') == 'on'
        contract.contractor = request.POST['contractor']
        contract.date = request.POST['date']
        contract.duration = request.POST['duration']
        contract.certification = Certification.objects.get(
            pk=certification_id)
        contract.admin = Employee.objects.get(pk=admin_id)
        contract.save()
        return redirect(reverse_lazy('contract:list'))
    else:
        return render(request, 'contract/update.html', context)
