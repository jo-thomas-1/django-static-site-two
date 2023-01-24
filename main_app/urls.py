from django.urls import path
from . import views # importing views module from current folder

urlpatterns = [
    path('', views.home, name='home')
]