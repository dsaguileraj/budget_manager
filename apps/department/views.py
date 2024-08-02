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
    query = request.GET.get('q', '')
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
            context['query_message'] = 'No se encontraron coincidencias'
    return render(request, 'department/list.html', context)


def detail_department(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        department = Department.objects.get(pk=pk)
        context = {'department': department}
    except Department.DoesNotExist:
        context = {'message': 'Departamento no encontrado'}
        return render(request, 'department/list.html', context)
    else:
        return render(request, 'department/detail.html', context)


def create_department(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    employees = Employee.objects.all()
    context = {'employees': employees}
    if request.method == 'POST':
        name = request.POST['name']
        director = Employee.objects.get(pk=request.POST['director'])
        try:
            department = Department.objects.create(
                name=name,
                director=director
            )
            department.save()
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'department/create.html', context)
        return redirect(reverse_lazy('department:list'))
    else:
        return render(request, 'department/create.html', context)


def delete_department(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return redirect(reverse_lazy('department:list'))
    except models.ProtectedError:
        return redirect(reverse_lazy('authentication:error'))
    department.delete()
    return redirect(reverse_lazy('department:list'))


def update_department(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    department = Department.objects.get(pk=pk)
    employees = Employee.objects.all()
    context = {
        'department': department,
        'employees': employees,
    }
    if request.method == 'POST':
        department.name = request.POST['name']
        department.director = request.POST['director']
        try:
            department.save()
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'department/update.html', context)
        return redirect(reverse_lazy('department:list'))
    else:
        return render(request, 'department/update.html', context)
