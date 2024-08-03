from decimal import Decimal
from django.core.paginator import Paginator
from django.db import IntegrityError, models
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
    except Certification.DoesNotExist:
        context = {'message': 'Certificación no encontrada'}
        return render(request, 'certification/list.html', context)
    except Exception as e:
        print(f'Error: {e}')
        return redirect(reverse_lazy('certification:list'))
    context = {'certification': certification}
    return render(request, 'certification/detail.html', context)


def create_certification(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {
        'procedures': Procedure.objects.all(),
        'budget_items': BudgetItem.objects.all(),
        'departments': Department.objects.all()
    }
    if request.method == 'POST':
        number = request.POST['number']
        budget = Decimal(request.POST['budget'])
        description = request.POST['description']
        try:
            budget_item = BudgetItem.objects.get(
                pk=request.POST['budget_item'])
            department = Department.objects.get(pk=request.POST['department'])
            procedure = Procedure.objects.get(pk=request.POST['procedure'])
        except BudgetItem.DoesNotExist:
            context['message'] = 'Partida seleccionada no existente'
            return render(request, 'certificaion/create.html', context)
        except Department.DoesNotExist:
            context['message'] = 'Departamento seleccionado no existente'
            return render(request, 'certificaion/create.html', context)
        except Procedure.DoesNotExist:
            context['message'] = 'Procedimiento seleccionado no existente'
            return render(request, 'certificaion/create.html', context)
        except Exception as e:
            print(f'Error: {e}')
            return redirect(reverse_lazy('certification:list'))
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
            except Exception as e:
                print(f'Error: {e}')
                return redirect(reverse_lazy('certification:list'))
            return redirect(reverse_lazy('certification:list'))
        else:
            context['message'] = 'El presupuesto a certificar excede el saldo disponible de la partida'
            return render(request, 'certification/create.html', context)
    else:
        return render(request, 'certification/create.html', context)


def delete_certification(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        certification = Certification.objects.get(pk=pk)
    except Certification.DoesNotExist:
        return redirect(reverse_lazy('certification:list'))
    try:
        certification.delete()
    except models.ProtectedError:
        return redirect(reverse_lazy('authentication:error'))
    except Exception as e:
        print(f'Error: {e}')
        return redirect(reverse_lazy('certification:list'))
    return redirect(reverse_lazy('certification:list'))


def update_certification(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        certification = Certification.objects.get(pk=pk)
    except Certification.DoesNotExist:
        return redirect(reverse_lazy('certification:list'))
    context = {
        'procedures': Procedure.objects.all(),
        'budget_items': BudgetItem.objects.all(),
        'departments': Department.objects.all(),
        'certification': certification,
    }
    if request.method == 'POST':
        certification.number = request.POST['number']
        certification.budget = Decimal(request.POST['budget'])
        certification.description = request.POST['description']
        try:
            certification.budget_item = BudgetItem.objects.get(
                pk=request.POST['budget_item'])
            certification.department = Department.objects.get(
                pk=request.POST['department'])
            certification.procedure = Procedure.objects.get(
                pk=request.POST['procedure'])
        except Procedure.DoesNotExist:
            context['message'] = 'Procedimiento seleccionado no existente'
            return render(request, 'certificaion/create.html', context)
        except BudgetItem.DoesNotExist:
            context['message'] = 'Partida seleccionada no existente'
            return render(request, 'certificaion/create.html', context)
        except Department.DoesNotExist:
            context['message'] = 'Departamento seleccionado no existente'
            return render(request, 'certificaion/create.html', context)
        except Exception as e:
            print(f'Error: {e}')
            return redirect(reverse_lazy('certification:list'))
        total_certification_budget = Certification.objects.filter(
            budget_item=certification.budget_item).aggregate(models.Sum('budget'))['budget__sum'] or 0
        if total_certification_budget + certification.budget <= certification.budget_item.budget:
            try:
                certification.save()
            except IntegrityError:
                context['message'] = 'Registro ya existente. Los siguientes campos, en conjunto, deben ser únicos: Número, Partida Presupuestaria'
                return render(request, 'certification/update.html', context)
            except Exception as e:
                print(f'Error: {e}')
                return redirect(reverse_lazy('certification:list'))
            return redirect(reverse_lazy('certification:list'))
        else:
            context['message'] = 'El presupuesto a certificar excede el saldo disponible de la partida'
            return render(request, 'certification/update.html', context)
    else:
        return render(request, 'certification/update.html', context)
