from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy("budget_items:list"))
        else:
            return render(request, "base.html", {"message": "Usuario y/o contraseña incorrectos"})
    return render(request, "base.html")


def user_logout(request):
    logout(request)
    return redirect(reverse_lazy("authentication:login"))
