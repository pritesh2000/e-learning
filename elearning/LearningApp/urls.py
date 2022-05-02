from django.urls import path
from . import views
from django.contrib import admin 

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("register/", views.register, name="register"),
    path("contact/", views.contact, name="contact"),
    path("myaccount/", views.myaccount, name="myaccount"),
    path("catinfo/<int:myid>/", views.catinfo, name="catinfo"),
    path("about/", views.about, name="about"),
    path("vplay/<int:myid>/", views.vplay, name="vplay"),
    path("search/", views.search, name="search"),
]