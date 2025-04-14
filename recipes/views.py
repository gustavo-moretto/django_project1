from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # django takes the views from template folder
    # you don't need specify the path
    return render(request, 'recipes/home.html') 

def contato(request):
    return render(request, 'index.html')

def sobre(request):
    return HttpResponse('Sobre')
