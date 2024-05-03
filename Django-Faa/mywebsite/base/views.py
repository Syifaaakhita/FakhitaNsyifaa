# from django.shortcuts import render 

# # Create your views here.

# # blog/views.py

# def home(request):
#     return render(request, 'base/home.html')
    
    #buat tes view
    
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the base index.")