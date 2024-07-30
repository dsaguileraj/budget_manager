from django.urls import path
from .views import list_contract, ContractDetailView, create_contract, delete_contract, update_contract

app_name = 'contract'

urlpatterns = [
    path('', list_contract, name='list'),
    path('create/', create_contract, name='create'),
    path('<str:pk>/', ContractDetailView.as_view(), name='detail'),
    path('delete/<str:pk>/', delete_contract, name='delete'),
    path('update/<str:pk>/', update_contract, name='update')
]
