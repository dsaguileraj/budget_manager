from django.urls import path
from .views import user_login, user_logout, error

app_name = "authentication"

urlpatterns = [
    path("", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("error/", error, name="error"),
]
