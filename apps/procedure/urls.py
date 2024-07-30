from django.urls import path
from .views import list_procedure, ProcedureDetailView, create_procedure, delete_procedure, update_procedure

app_name = 'procedure'

urlpatterns = [
    path('', list_procedure, name = 'list'),
    path('create/', create_procedure, name = 'create'),
    path('<str:pk>/', ProcedureDetailView.as_view(), name = 'detail'),    
    path('delete/<str:pk>/', delete_procedure, name = 'delete'),
    path('update/<str:pk>/', update_procedure, name = 'update')
]
