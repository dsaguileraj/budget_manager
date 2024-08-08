from django.db import models, IntegrityError
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Department, Employee


def list_department(request: HttpRequest) -> HttpResponse:
    object_list = Department.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    query = request.GET.get('q', '').strip()
    if query:
        result = Department.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(director__first_name__icontains=query) |
            models.Q(director__middle_name__icontains=query) |
            models.Q(director__first_last_name__icontains=query) |
            models.Q(director__middle_last_name__icontains=query) |
            models.Q(director__ci__icontains=query)
        ).order_by('name')
        if result:
            context['page_obj'] = result
        if not result:
            context['message'] = 'No se encontraron coincidencias'
    return render(request, 'department/list.html', context)


def detail_department(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        context = {'message': 'Departamento no encontrado'}
        return render(request, 'department/list.html', context)
    except Exception as error:
        context = {'Exception': error}
        return render(request, 'department/list.html', context)
    else:
        context = {'department': department}
        return render(request, 'department/detail.html', context)


def create_department(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    context = {'employees': Employee.objects.all()}
    if request.method == 'POST':
        name = request.POST.get('name')
        director = Employee.objects.get(pk=request.POST.get('director'))
        try:
            department = Department.objects.create(
                name=name.strip(),
                director=director
            )
        except IntegrityError as error:
            context['IntegrityError'] = error
            return render(request, 'department/create.html', context)
        except Exception as error:
            context['Exception'] = error
            return render(request, 'department/create.html', context)
        else:
            department.save()
            return redirect(reverse_lazy('department:list'))
    else:
        return render(request, 'department/create.html', context)


def delete_department(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        context = {'message': 'Departamento no encontrado'}
        return render(request, 'department/list.html', context)
    except Exception as error:
        context = {'Exception': error}
        return render(request, 'department/list.html', context)
    try:
        department.delete()
    except models.ProtectedError as error:
        context = {'ProtectedError': error}
        return render(request, 'department/list.html', context)
    except Exception as error:
        context = {'Exception': error}
        return render(request, 'department/list.html', context)
    else:
        return redirect(reverse_lazy('department:list'))


def update_department(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        context = {'message': 'Departamento no encontrado'}
        return render(request, 'department/list.html', context)
    except Exception as error:
        context = {'Exception': error}
        return render(request, 'department/list.html', context)
    else:
        context = {
            'department': department,
            'employees': Employee.objects.all(),
        }
    if request.method == 'POST':
        department.name = request.POST.get('name').strip()
        department.director = request.POST.get('director')
        try:
            department.save()
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'department/update.html', context)
        except Exception as error:
            context['Exception'] = error
            return render(request, 'department/update.html', context)
        else:
            return redirect(reverse_lazy('department:detail', args=[pk]))
    else:
        return render(request, 'department/update.html', context)
