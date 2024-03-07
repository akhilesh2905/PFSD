from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name="home"),
    path("login", views.loginPage, name="login"),
    path("about", views.aboutPage, name="about"),
    path("contact", views.contactPage, name="contact"),


]