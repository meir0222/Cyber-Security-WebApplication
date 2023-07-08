from django.urls import path,include
from . import views

app_name = "users"

urlpatterns = [

 path('', views.home, name = "home"),
 path('login', views.Login, name="login"),
 path("signup/", views.SignUp, name="signup"),
 path('customers', views.customers, name="customers"),
 path('search_customers', views.search_customers, name='search_customers'),
 path('send_email', views.send_email, name='send_email'),
 path('validate_email', views.validate_email, name='validate_email'),






]