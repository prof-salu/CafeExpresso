from django.contrib import admin
from django.urls import path
from cafe.views.FilialViews import *

urlpatterns = [
    path('', lista_filial_view),
]

