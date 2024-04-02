from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def budget_items(request):
    return render(request, "budget_items.html")


def certifications(request):
    return render(request, "certifications.html")