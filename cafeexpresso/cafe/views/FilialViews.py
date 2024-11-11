from django.http import HttpResponse
from django.shortcuts import render
from cafe.models.Filial import *


def lista_filial_view(request):
    lista_filiais = Filial.objects.all()

    context = {
        'lista_filiais' : lista_filiais
    }

    return render(request, 'cafeexpresso/index.html', context)
