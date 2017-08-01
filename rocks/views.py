from django.shortcuts import render

from .models import Rock


def index(request):
    """Returns index view showing a list of all rocks"""
    rocks = Rock.objects.all()
    return render(request, 'rocks/index.html', {'rocks': rocks})


def detail(request, rock_name):
    """Returns a detail view of a specific rock and its properties"""
    get_rock = Rock.objects.get(name=rock_name)
    return render(request, 'rocks/detail.html', {'rock': get_rock})
