from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'rocks/index.html')


def detail(request):
    return render(request, 'rocks/detail.html')
