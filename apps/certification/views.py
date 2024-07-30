from decimal import Decimal
from django.db import IntegrityError, models
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import BudgetItem, Certification, Department, Procedure


def list_certification(request: HttpRequest) -> HttpResponse:
    object_list = Certification.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    query = request.GET.get('q', '')
    if query:
        result = Certification.objects.filter(
            models.Q(number__icontains=query) |
            models.Q(budget_item__number__icontains=query) |
            models.Q(description__icontains=query) |
            models.Q(budget_item__activity__icontains=query) |
            models.Q(budget__icontains=query)
        ).order_by('number')
        if result:
            context['page_obj'] = result
        if not result:
            context['query_message'] = 'No se encontraron coincidencias'
    return render(request, 'certification/list.html', context)


def detail_certification(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        certification = Certification.objects.get(pk=pk)
        context = {'certification': certification}
    except Certification.DoesNotExist:
        context = {'message': 'Certificación no encontrada'}
        return render(request, 'certification/list.html', context)
    else:
        return render(request, 'certification/detail.html', context)


def create_certification(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {
        'procedures': Procedure.objects.all(),
        'budget_items': BudgetItem.objects.all(),
        'departments': Department.objects.all()
    }
    if request.method == 'POST':
        number = request.POST['number']
        procedure_id = request.POST['procedure']
        budget_item_id = request.POST['budget_item']
        department_id = request.POST['department']
        budget = Decimal(request.POST['budget'])
        description = request.POST['description']
        procedure = Procedure.objects.get(pk=procedure_id)
        budget_item = BudgetItem.objects.get(pk=budget_item_id)
        department = Department.objects.get(pk=department_id)
        total_certification_budget = Certification.objects.filter(
            budget_item=budget_item).aggregate(models.Sum('budget'))['budget__sum'] or 0
        if total_certification_budget + budget <= budget_item.budget:
            try:
                certification = Certification.objects.create(
                    number=number,
                    procedure=procedure,
                    budget_item=budget_item,
                    department=department,
                    budget=budget,
                    description=description,
                )
                certification.save()
            except IntegrityError:
                context['message'] = 'Registro ya existente. Los siguientes campos, en conjunto, deben ser únicos: Número, Partida Presupuestaria'
                return render(request, 'certification/create.html', context)
            return redirect(reverse_lazy('certification:list'))
        else:
            context['message'] = 'El presupuesto a certificar excede el saldo disponible de la partida'
            return render(request, 'certification/create.html', context)
    else:
        return render(request, 'certification/create.html', context)


def delete_certification(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        certification = Certification.objects.get(pk=pk)
        certification.delete()
        deleted = True
    except Certification.DoesNotExist:
        deleted = False
    except models.ProtectedError:
        return redirect(reverse_lazy('authentication:error'))
    if deleted:
        return redirect(reverse_lazy('certification:list'))
    else:
        return render(request, 'certification/list.html')


def update_certification(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    certification = Certification.objects.get(pk=pk)
    context = {
        'procedures': Procedure.objects.all(),
        'budget_items': BudgetItem.objects.all(),
        'departments': Department.objects.all(),
        'certification': certification,
    }
    if request.method == 'POST':
        procedure_id = request.POST['procedure']
        budget_item_id = request.POST['budget_item']
        department_id = request.POST['department']
        certification.number = request.POST['number']
        certification.budget = Decimal(request.POST['budget'])
        certification.description = request.POST['description']
        certification.procedure = Procedure.objects.get(pk=procedure_id)
        certification.budget_item = BudgetItem.objects.get(pk=budget_item_id)
        certification.department = Department.objects.get(pk=department_id)
        total_certification_budget = Certification.objects.filter(
            budget_item=certification.budget_item).aggregate(models.Sum('budget'))['budget__sum'] or 0
        if total_certification_budget + certification.budget <= certification.budget_item.budget:
            try:
                certification.save()
                return redirect(reverse_lazy('certification:list'))
            except IntegrityError:
                context['message'] = 'Registro ya existente. Los siguientes campos, en conjunto, deben ser únicos: Número, Partida Presupuestaria'
                return render(request, 'certification/update.html', context)
        else:
            context['message'] = 'El presupuesto a certificar excede el saldo disponible de la partida'
            return render(request, 'certification/update.html', context)
    else:
        return render(request, 'certification/update.html', context)
