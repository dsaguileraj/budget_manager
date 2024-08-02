from django.db import IntegrityError, models
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Employee


def list_employee(request: HttpRequest) -> HttpResponse:
    object_list = Employee.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    query = request.GET.get('q', '')
    if query:
        result = Employee.objects.filter(
            models.Q(ci__icontains=query) |
            models.Q(first_name__icontains=query) |
            models.Q(middle_name__icontains=query) |
            models.Q(first_last_name__icontains=query) |
            models.Q(middle_last_name__icontains=query) |
            models.Q(email__icontains=query) |
            models.Q(user__icontains=query)
        ).order_by('first_last_name', 'middle_last_name', 'first_name', 'middle_name', 'ci')
        if result:
            context['page_obj'] = result
        if not result:
            context['query_message'] = 'No se encontraron coincidencias'
    return render(request, 'employee/list.html', context)


def detail_employee(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        employee = Employee.objects.get(pk=pk)
        context = {'employee': employee}
    except Employee.DoesNotExist:
        context = {'message': 'Empleado no encontrado'}
        return render(request, 'employee/list.html', context)
    else:
        return render(request, 'employee/detail.html', context)


def create_employee(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        ci = request.POST['ci']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        first_last_name = request.POST['first_last_name']
        middle_last_name = request.POST['middle_last_name']
        email = request.POST['email']
        user = request.POST['user']
        try:
            employee = Employee.objects.create(
                ci=ci,
                first_name=first_name,
                middle_name=middle_name,
                first_last_name=first_last_name,
                middle_last_name=middle_last_name,
                email=email,
                user=user
            )
            employee.save()
        except IntegrityError:
            context = {'message': 'Registro ya existente'}
            return render(request, 'employee/create.html', context)
        return redirect(reverse_lazy('employee:list'))
    else:
        return render(request, 'employee/create.html')


def delete_employee(request: HttpRequest, pk: str) -> HttpResponse | HttpResponseRedirect:
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return redirect(reverse_lazy('employee:list'))
    except models.ProtectedError:
        return redirect(reverse_lazy('authentication:error'))
    employee.delete()
    return redirect(reverse_lazy('employee:list'))


def update_employee(request: HttpRequest, pk: str) -> HttpResponse | HttpResponseRedirect:
    employee = Employee.objects.get(pk=pk)
    context = {'employee': employee}
    if request.method == 'POST':
        employee.ci = request.POST['ci']
        employee.first_name = request.POST['first_name']
        employee.middle_name = request.POST['middle_name']
        employee.first_last_name = request.POST['first_last_name']
        employee.middle_last_name = request.POST['middle_last_name']
        employee.email = request.POST['email']
        employee.user = request.POST['user']
        try:
            employee.save()
            return redirect(reverse_lazy('employee:list'))
        except IntegrityError:
            context['message'] = 'Registro ya existente'
            return render(request, 'employee/update.html', context)
    else:
        return render(request, 'employee/update.html', context)
