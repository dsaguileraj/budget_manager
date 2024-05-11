from django.urls import path
from .views import *

app_name = "authentication"

urlpatterns = [
    path("", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]
