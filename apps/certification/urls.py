from django.urls import path
from . import views

app_name = 'certification'

urlpatterns = [
    path('', views.list_certification, name='list'),
    path('create/', views.create_certification, name='create'),
    path('<int:pk>/', views.detail_certification, name='detail'),
    path('delete/<int:pk>/', views.delete_certification, name='delete'),
    path('update/<int:pk>/', views.update_certification, name='update')
]
