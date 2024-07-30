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
        'certifications': Certification.objects.all()
    }
    if request.method == 'POST':
        number = request.POST['number']
        certifications = request.POST.getlist('certifications')
        admin_id = request.POST['admin']
        contractor = request.POST['contractor']
        suscription = request.POST['suscription']
        duration = request.POST['duration']

        try:
            admin = Employee.objects.get(pk=admin_id)
        except Employee.DoesNotExist:
            context['message'] = 'Empleado no encontrado'
            return render(request, 'contract/create.html', context)

        try:
            contract = Contract.objects.create(
                number=number,
                admin=admin,
                contractor=contractor,
                suscription=suscription,
                duration=duration,
            )
            contract.certification.set(certifications)
            # contract.save()

        # id = request.POST['id']
        # certification_id = request.POST['certification']
        # admin_id = request.POST['admin']
        # contractor = request.POST['contractor']
        # date = request.POST['date']
        # duration = request.POST['duration']
        # certification = Certification.objects.get(pk=certification_id)
        # admin = Employee.objects.get(pk=admin_id)
        # try:
        #     contract = Contract.objects.create(
        #         id=id,
        #         certification=certification,
        #         admin=admin,
        #         contractor=contractor,
        #         date=date,
        #         duration=duration
        #     )
        #     contract.save()
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'contract/create.html', context)
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


def update_contract(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    contract = Contract.objects.get(pk=pk)
    context = {
        'employees': Employee.objects.all(),
        'certifications': Certification.objects.all(),
        'contract': contract
    }
    if request.method == 'POST':
        contract.number = request.POST['number']
        certifications = request.POST.getlist('certifications')
        contract.certification.set(certifications)
        admin_id = request.POST['admin']
        contract.admin = Employee.objects.get(pk=admin_id)
        contract.contractor = request.POST['contractor']
        contract.suscription = request.POST['suscription']
        contract.duration = request.POST['duration']
        
        # admin_id = request.POST['admin']
        # certification_id = request.POST['certification']
        # contract.pk = request.POST['id']
        # contract.advance = request.POST.get('advance') == 'on'
        # contract.contractor = request.POST['contractor']
        # contract.date = request.POST['date']
        # contract.duration = request.POST['duration']
        # contract.certification = Certification.objects.get(
        #     pk=certification_id)
        # contract.admin = Employee.objects.get(pk=admin_id)
        
        try:
            contract.save()
            return redirect(reverse_lazy('contract:list'))
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'contract/update.html', context)    
    else:
        return render(request, 'contract/update.html', context)
