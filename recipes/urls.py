from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from recipes.views import home, contato, sobre


urlpatterns = [    
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
