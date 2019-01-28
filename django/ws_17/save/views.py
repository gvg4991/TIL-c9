from django.shortcuts import render
from .models import Save

# Create your views here.
def create(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    birthday = request.GET.get('birthday')
    age = request.GET.get('age')
    