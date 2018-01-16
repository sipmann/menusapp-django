from django.contrib import admin
from django.urls import path

from . import views

app_name = 'comentarios'

urlpatterns = [
    path('listagem', views.listagem, name='listagem'),
]
