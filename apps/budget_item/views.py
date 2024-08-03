import pandas
from django.db import IntegrityError, models
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from apps.core.choices import BudgetType
from .models import BudgetItem


def list_budget_item(request: HttpRequest) -> HttpResponse:
    object_list = BudgetItem.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total = BudgetItem.objects.aggregate(
        total_budget=models.Sum('budget'))['total_budget']
    context = {
        'page_obj': page_obj,
        'total_budget': f'{total: .2f}' if total else 0}
    query = request.GET.get('q', '')
    if query:
        result = BudgetItem.objects.filter(
            models.Q(number__icontains=query) |
            models.Q(cpc__icontains=query) |
            models.Q(description__icontains=query) |
            models.Q(activity__icontains=query) |
            models.Q(budget__icontains=query)
        ).order_by('number')
        if result:
            context['page_obj'] = result
        if not result:
            context['message'] = 'No se encontraron coincidencias'
    return render(request, 'budget_item/list.html', context)


def detail_budget_item(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        budget_item = BudgetItem.objects.get(pk=pk)
    except BudgetItem.DoesNotExist:
        context = {'message': 'Partida presupuestaria no encontrada'}
        return render(request, 'budget_item/list.html', context)
    except Exception as error:
        context = {'Exception': error}
        return render(request, 'budget_item/list.html', context)
    context = {'budget_item': budget_item}
    return render(request, 'budget_item/detail.html', context)


def create_budget_item(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {'budget_types': BudgetType.choices}
    if request.method == 'POST':
        number = request.POST['number']
        cpc = request.POST['cpc']
        budget = request.POST['budget']
        budget_type = request.POST['budget_type']
        description = request.POST['description']
        activity = request.POST['activity']
        bid = request.POST.get('bid') == 'on'
        c1 = request.POST.get('c1') == 'on'
        c2 = request.POST.get('c2') == 'on'
        c3 = request.POST.get('c3') == 'on'
        try:
            budget_item = BudgetItem.objects.create(
                number=number,
                cpc=cpc,
                budget=budget,
                budget_type=budget_type,
                description=description,
                activity=activity,
                bid=bid,
                c1=c1,
                c2=c2,
                c3=c3,
            )
            budget_item.save()
        except IntegrityError as error:
            context['IntegrityError'] = error
            return render(request, 'budget_item/create.html', context)
        except Exception as error:
            context = {'Exception': error}
            return render(request, 'budget_item/list.html', context)
        return redirect(reverse_lazy('budget_item:list'))
    else:
        return render(request, 'budget_item/create.html', context)


def delete_budget_item(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        budget_item = BudgetItem.objects.get(pk=pk)
    except BudgetItem.DoesNotExist:
        context = {'message': 'Partida presupuestaria no encontrada'}
        return render(request, 'budget_item/list.html', context)
    try:
        budget_item.delete()
    except models.ProtectedError as error:
        context = {'ProtectedError': error}
        return render(request, 'budget_item/list.html', context)
    except Exception as error:
        context = {'Exception': error}
        return render(request, 'budget_item/list.html', context)
    return redirect(reverse_lazy('budget_item:list'))


def update_budget_item(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        budget_item = BudgetItem.objects.get(pk=pk)
    except BudgetItem.DoesNotExist:
        context = {'message': 'Partida presupuestaria no encontrada'}
        return render(request, 'budget_item/update.html', context)
    context = {
        'budget_item': budget_item,
        'budget_types': BudgetType.choices
    }
    if request.method == 'POST':
        budget_item.number = request.POST['number']
        budget_item.cpc = request.POST['cpc']
        budget_item.budget = request.POST['budget']
        budget_item.budget_type = request.POST['budget_type']
        budget_item.description = request.POST['description']
        budget_item.activity = request.POST['activity']
        budget_item.bid = request.POST.get('bid') == 'on'
        budget_item.c1 = request.POST.get('c1') == 'on'
        budget_item.c2 = request.POST.get('c2') == 'on'
        budget_item.c3 = request.POST.get('c3') == 'on'
        try:
            budget_item.save()
        except IntegrityError as error:
            context['IntegrityError'] = error
            return render(request, 'budget_item/update.html', context)
        except Exception as error:
            context = {'Exception': error}
            return render(request, 'budget_item/list.html', context)
        return redirect(reverse_lazy('budget_item:detail', args=[pk]))
    else:
        return render(request, 'budget_item/update.html', context)


def upload_file(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        file = request.FILES['file']
        data = pandas.read_excel(file, engine='openpyxl')
        for index, row in data.iterrows():
            try:
                BudgetItem.objects.create(
                    number=row['Número'],
                    cpc=row['CPC'],
                    budget=row['Presupuesto'],
                    budget_type=row['Tipo de Presupuesto'],
                    description=row['Descripción'],
                    activity=row['Actividad'],
                    bid=row['BID'],
                    c1=row['C1'],
                    c2=row['C2'],
                    c3=row['C3'],
                )
            except KeyError:
                context = {'message': f'ERROR: Fila no. {index + 1} inválida'}
                return render(request, 'budget_item/create_excel.html', context)
            except Exception as error:
                context = {'Exception': error}
                return render(request, 'budget_item/list.html', context)
        return redirect(reverse_lazy('budget_item:list'))
    return render(request, 'budget_item/create_excel.html')
