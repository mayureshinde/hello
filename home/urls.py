from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("home", views.index, name="home"),
    path("login", views.loginUser, name="login"),
    path('logout', views.logoutUser, name='logout'),
    path('registration', views.registration, name="registration")
] 