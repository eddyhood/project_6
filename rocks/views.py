from django.shortcuts import render

from .models import Rock

# Create your views here.


def index(request):
    rocks = Rock.objects.all()

    return render(request, 'rocks/index.html', {'rocks': rocks})


def detail(request):
    return render(request, 'rocks/detail.html')
