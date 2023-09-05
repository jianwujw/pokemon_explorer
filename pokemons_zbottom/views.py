from django.shortcuts import render
from .models import *





def index(request):
    pokemons = Pokemon.objects.all()
    return render(request,'index.html', {'pokemons':pokemons})


# Create your views here.
