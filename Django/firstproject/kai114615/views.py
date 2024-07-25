from django.shortcuts import render
from .models import Sakila

# Create your views here.

def index(request):
    id = request.Get.get('id', 1)
    
    return render(request, 'index.html')


def countries(request):
    countries = Sakila.countries()
    return render(request, 'countries.html', {'countries':countries})