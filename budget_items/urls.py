from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("budget_items/", views.budget_items, name = "budget_items"),
    path("certifications/", views.certifications, name = "certifications"),
]