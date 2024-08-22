from django.db import IntegrityError, models
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Employee


def list_employee(request: HttpRequest) -> HttpResponse:
    object_list = Employee.objects.all()
    paginator = Paginator(object_list, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    query = request.GET.get("q", "").strip()
    if query:
        result = Employee.objects.filter(
            models.Q(ci__icontains=query) |
            models.Q(first_name__icontains=query) |
            models.Q(middle_name__icontains=query) |
            models.Q(first_last_name__icontains=query) |
            models.Q(middle_last_name__icontains=query) |
            models.Q(email__icontains=query) |
            models.Q(user__icontains=query)
        ).order_by("first_last_name", "middle_last_name", "first_name", "middle_name", "ci")
        if result:
            context["page_obj"] = result
        if not result:
            context["message"] = "No se encontraron coincidencias"
    return render(request, "employee/list.html", context)


def detail_employee(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        context = {"message": "Empleado no encontrado"}
        return render(request, "employee/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "employee/list.html", context)
    else:
        context = {"employee": employee}
        return render(request, "employee/detail.html", context)


def create_employee(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        ci = request.POST.get("ci")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        first_last_name = request.POST.get("first_last_name")
        middle_last_name = request.POST.get("middle_last_name")
        email = request.POST.get("email")
        user = request.POST.get("user")
        try:
            employee = Employee.objects.create(
                ci=ci.strip(),
                first_name=first_name.strip(),
                middle_name=middle_name.strip(),
                first_last_name=first_last_name.strip(),
                middle_last_name=middle_last_name.strip(),
                email=email.strip(),
                user=user.strip(),
            )
        except IntegrityError as error:
            context = {"IntegrityError": error}
            return render(request, "employee/create.html", context)
        except Exception as error:
            context = {"Exception": error}
            return render(request, "employee/create.html", context)
        else:
            employee.save()
            return redirect(reverse_lazy("employee:list"))
    else:
        return render(request, "employee/create.html")


def delete_employee(request: HttpRequest, pk: str) -> HttpResponse | HttpResponseRedirect:
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        context = {"message": "Empleado no encontrado"}
        return render(request, "employee/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "employee/list.html", context)
    try:
        employee.delete()
    except models.ProtectedError as error:
        context = {"ProtectedError": error}
        return render(request, "employee/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "employee/list.html", context)
    else:
        return redirect(reverse_lazy("employee:list"))


def update_employee(request: HttpRequest, pk: str) -> HttpResponse | HttpResponseRedirect:
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        context = {"message": "Empleado no encontrado"}
        return render(request, "employee/list.html", context)
    except Exception as error:
        context = {"Exception": error}
        return render(request, "employee/list.html", context)
    else:
        context = {"employee": employee}
    if request.method == "POST":
        employee.ci = request.POST.get("ci").strip()
        employee.first_name = request.POST.get("first_name").strip()
        employee.middle_name = request.POST.get("middle_name").strip()
        employee.first_last_name = request.POST.get("first_last_name").strip()
        employee.middle_last_name = request.POST.get("middle_last_name").strip()
        employee.email = request.POST.get("email").strip()
        employee.user = request.POST.get("user").strip()
        try:
            employee.save()
        except IntegrityError as error:
            context["IntegrityError"] = error
            return render(request, "employee/update.html", context)
        except Exception as error:
            context["Exception"] = error
            return render(request, "employee/update.html", context)
        else:
            return redirect(reverse_lazy("employee:detail", args=[pk]))
    else:
        return render(request, "employee/update.html", context)
