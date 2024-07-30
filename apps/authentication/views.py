from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy("budget_item:list"))
        else:
            return render(request, "base.html", {"message": "Usuario y/o contraseña incorrectos"})
    return render(request, "base.html")


def user_logout(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    return redirect(reverse_lazy("authentication:login"))


def error(request):
    return render(request, "base.html", {"message": "No se puedo eliminar el registro porque está siendo referenciado por otros registros. Para eliminarlo, primero elimine los otros registros que los referencia."})
