from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # django takes the views from template folder
    # you don't need specify the path
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Gustavo',        
    }) 

def recipe(request, id):
    # django takes the views from template folder
    # you don't need specify the path
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Gustavo',        
    }) 

