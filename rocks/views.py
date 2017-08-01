from django.shortcuts import render

from .models import Rock

# Create your views here.


def index(request):
    rocks = Rock.objects.all()
    return render(request, 'rocks/index.html', {'rocks': rocks})


def detail(request, rock_name):
    get_rock = Rock.objects.get(name=rock_name)
    return render(request, 'rocks/detail.html', {'rock': get_rock})
