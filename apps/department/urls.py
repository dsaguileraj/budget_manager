from django.urls import path
from .views import list_department, DepartmentDetailView, create_department, delete_department, update_department

app_name = 'department'

urlpatterns = [
    path('', list_department, name='list'),
    path('create/', create_department, name='create'),
    path('<str:pk>/', DepartmentDetailView.as_view(), name='detail'),
    path('delete/<str:pk>/', delete_department, name='delete'),
    path('update/<str:pk>/', update_department, name='update')
]
