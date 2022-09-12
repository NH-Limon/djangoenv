from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello Django!😇</h1>')
