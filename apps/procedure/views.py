from django.db import models, IntegrityError
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Procedure, ProductType, PurchaseType, Regime


def list_procedure(request: HttpRequest) -> HttpResponse:
    object_list = Procedure.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    query = request.GET.get('q', '')
    if query:
        result = Procedure.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(regime__icontains=query) |
            models.Q(product_type__icontains=query) |
            models.Q(purchase_type__icontains=query)
        ).order_by('name')
        if result:
            context['page_obj'] = result
        if not result:
            context['query_message'] = 'No se encontraron coincidencias'
    return render(request, 'procedure/list.html', context)


def detail_procedure(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        procedure = Procedure.objects.get(pk=pk)
        context = {'procedure': procedure}
    except Procedure.DoesNotExist:
        context = {'message': 'Procedimiento no encontrado'}
        return render(request, 'procedure/list.html', context)
    else:
        return render(request, 'procedure/detail.html', context)


def create_procedure(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {
        'regimes': Regime.choices,
        'product_types': ProductType.choices,
        'purchase_types': PurchaseType.choices,
    }
    if request.method == 'POST':
        name = request.POST['name']
        regime = request.POST['regime']
        product_type = request.POST['product_type']
        purchase_type = request.POST['purchase_type']
        try:
            procedure = Procedure.objects.create(
                name=name,
                regime=regime,
                product_type=product_type,
                purchase_type=purchase_type
            )
            procedure.save()
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'procedure/create.html', context)
        return redirect(reverse_lazy('procedure:list'))
    else:
        return render(request, 'procedure/create.html', context)


def delete_procedure(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        procedure = Procedure.objects.get(pk=pk)
    except Procedure.DoesNotExist:
        return redirect(reverse_lazy('procedure:list'))
    except models.ProtectedError:
        return redirect(reverse_lazy('authentication:error'))
    procedure.delete()
    return redirect(reverse_lazy('procedure:list'))


def update_procedure(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    procedure = Procedure.objects.get(pk=pk)
    context = {
        'regimes': Regime.choices,
        'product_types': ProductType.choices,
        'purchase_types': PurchaseType.choices,
        'procedure': procedure
    }
    if request.method == 'POST':
        procedure.name = request.POST['name']
        procedure.regime = request.POST['regime']
        procedure.product_type = request.POST['product_type']
        procedure.purchase_type = request.POST['purchase_type']
        try:
            procedure.save()
            return redirect(reverse_lazy('procedure:list'))
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'procedure/update.html', context)
    else:
        return render(request, 'procedure/update.html', context)
