from django.urls import path
from .views import list_budget_item, BudgetItemDetailView, create_budget_item, delete_budget_item, update_budget_item, upload_file

app_name = 'budget_item'

urlpatterns = [
    path('', list_budget_item, name='list'),
    path('create/', create_budget_item, name='create'),
    path('upload/', upload_file, name='upload'),
    path('<int:pk>/', BudgetItemDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', delete_budget_item, name='delete'),
    path('update/<int:pk>/', update_budget_item, name='update')
]
