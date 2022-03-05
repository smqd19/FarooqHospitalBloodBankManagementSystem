from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('contacts.html', views.contact, name="contact"),
    path('chartpage.html', views.charts, name="charts"),
]