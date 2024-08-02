from django.urls import path
from . import views

app_name = 'department'

urlpatterns = [
    path('', views.list_department, name='list'),
    path('create/', views.create_department, name='create'),
    path('<str:pk>/', views.detail_department, name='detail'),
    path('delete/<str:pk>/', views.delete_department, name='delete'),
    path('update/<str:pk>/', views.update_department, name='update')
]
