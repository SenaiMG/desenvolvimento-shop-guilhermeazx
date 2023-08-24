from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render( request, 'index.html')

def carrinho(request):
    return render( request, 'carrinho.html')