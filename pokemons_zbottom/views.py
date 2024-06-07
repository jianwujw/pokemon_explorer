from django.shortcuts import render
from .models import *





def index(request):
    
    pokemons = Pokemon.objects.all()
    ordered_moves = Moves.objects.all().order_by('level_learned')
    for pokemon in pokemons:
        ordered_moves =pokemon.moves.order_by('level_learned')


    return render(request,'index.html', {'pokemons':pokemons,'ordered_moves':ordered_moves})

def info(request, id):
    pokemon = Pokemon.objects.get(id=id)
    #sort our moves by level learned using lambda
    sortedmoves = sorted(pokemon.moves.all(),key =lambda x: x.level_learned)
    return render(request,'info.html',{'pokemon':pokemon,'sortedmoves':sortedmoves})




# Create your views here.
