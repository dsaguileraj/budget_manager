from django.urls import path
from .views import list_employee, EmployeeDetailView, create_employee, delete_employee, update_employee

app_name = 'employee'

urlpatterns = [
    path('', list_employee, name='list'),
    path('create/', create_employee, name='create'),
    path('<str:pk>/', EmployeeDetailView.as_view(), name='detail'),
    path('delete/<str:pk>/', delete_employee, name='delete'),
    path('update/<str:pk>/', update_employee, name='update')
]
