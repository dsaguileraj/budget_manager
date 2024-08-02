from datetime import datetime
from django.db import IntegrityError, models
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Contract, Certification, Employee


def list_contract(request: HttpRequest) -> HttpResponse:
    object_list = Contract.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    query = request.GET.get('q', '')
    if query:
        result = Contract.objects.filter(
            models.Q(number__icontains=query) |
            models.Q(certification__description__icontains=query) |
            models.Q(certification__budget__icontains=query) |
            models.Q(admin__first_name__icontains=query) |
            models.Q(admin__middle_name__icontains=query) |
            models.Q(admin__first_last_name__icontains=query) |
            models.Q(admin__middle_last_name__icontains=query) |
            models.Q(contractor__icontains=query)
        ).order_by('number')
        if result:
            context['page_obj'] = result
        if not result:
            context['query_message'] = 'No se encontraron coincidencias'
    return render(request, 'contract/list.html', context)


def detail_contract(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        contract = Contract.objects.get(pk=pk)
        context = {'contract': contract}
    except IntegrityError:
        context = {'message': 'Contrato no encontrado'}
        return render(request, 'contract/list.html', context)
    else:
        return render(request, 'contract/detail.html', context)


def create_contract(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {
        'employees': Employee.objects.all(),
        'certifications': Certification.objects.all(),
    }
    if request.method == 'POST':
        number = request.POST.get('number')
        contractor = request.POST.get('contractor')
        suscription_str = request.POST.get('suscription')
        duration = request.POST.get('duration')
        selected_certifications = request.POST.getlist('certification')

        try:
            admin = Employee.objects.get(pk=request.POST.get('admin'))
        except Employee.DoesNotExist:
            context = {'message': 'El administrador seleccionado no existe'}
            return render(request, 'contract/create.html', context)

        try:
            new_contract = Contract.objects.create(
                number=number,
                admin=admin,
                contractor=contractor,
                suscription=datetime.strptime(
                    suscription_str, '%Y-%m-%d').date(),
                duration=duration,
            )
            certs = Certification.objects.filter(
                pk__in=selected_certifications)
            new_contract.certification.add(*certs)
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'contract/create.html', context)

        return redirect(reverse_lazy('contract:list'))
    else:
        return render(request, 'contract/create.html', context)


def delete_contract(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        return redirect(reverse_lazy('contract:list'))
    except models.ProtectedError:
        return redirect(reverse_lazy('authentication:error'))
    contract.delete()
    return redirect(reverse_lazy('contract:list'))


def update(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    contract = Contract.objects.get(pk=pk)
    context = {
        'employees': Employee.objects.all(),
        'certifications': Certification.objects.all(),
        'contract': Contract.objects.get(pk=pk),
    }
    if request.method == 'POST':
        selected_certifications = request.POST.getlist('certification')
        suscription_str = request.POST.get('suscription')

        contract.number = request.POST.get('number')
        contract.contractor = request.POST.get('contractor')
        contract.duration = request.POST.get('duration')
        contract.suscription = datetime.strptime(
            suscription_str, '%Y-%m-%d').date(),

        try:
            contract.admin = Employee.objects.get(pk=request.POST.get('admin'))
        except Employee.DoesNotExist:
            context = {'message': 'Administrador seleccionado no existente'}
            return render(request, 'contract/create.html', context)

        try:
            certs = Certification.objects.filter(
                pk__in=selected_certifications)
            contract.certification.add(*certs)
            contract.save()
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'contract/update.html', context)

        return redirect(reverse_lazy('contract:list'))
    else:
        return render(request, 'contract/update.html', context)
