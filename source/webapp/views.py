from django.shortcuts import render
from django.views.generic import ListView


def index_view(request):
    return render(request, 'index.html', locals())


def catalogue(request):
    return render(request, 'catalogue.html', locals())
