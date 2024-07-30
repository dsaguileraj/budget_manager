from django.db import models, IntegrityError
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Department, Employee


def list_department(request: HttpRequest) -> HttpResponse:
    object_list = Department.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': object_list,
        'page_obj': page_obj,
    }
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
            context['object_list'] = result
        if not result:
            context['query_message'] = 'No se encontraron coincidencias'
    return render(request, 'department/list.html', context)


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department/detail.html'


def create_department(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
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
            return render(request, 'department/create.html', {'employees': Employee.objects.all(), 'message': 'Registro ya existente'})
        return redirect(reverse_lazy('department:list'))
    else:
        return render(request, 'department/create.html', {'employees': Employee.objects.all()})


def delete_department(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    try:
        department = Department.objects.get(pk=pk)
        department.delete()
        deleted = True
    except Department.DoesNotExist:
        deleted = False
    except models.ProtectedError:
        return redirect(reverse_lazy('authentication:error'))
    if deleted:
        return redirect(reverse_lazy('department:list'))
    else:
        return render(request, 'department/list.html')


def update_department(request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
        department.name = request.POST['name']
        department.director = request.POST['director']
        try:
            department.save()
        except IntegrityError:
            return render(request, 'department/update.html', {'department': department, 'message': 'Registro ya existente'})
        return redirect(reverse_lazy('department:list'))
    else:
        return render(request, 'department/update.html', {'department': department})
