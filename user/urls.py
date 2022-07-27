from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login", views.Login, name="login"),
    path("register", views.Register, name="register"),
    path("info/<profile_id>", views.CompanyInfo, name="companyInfo"),
]