from django.core.management.base import BaseCommand
from pokemons_zbottom.models import *
import requests
import time
import sqlite3

class Command(BaseCommand):
    def handle(self, *args, **options):
        pokemon_count = 1281
        for pokemon in range(1,pokemon_count):
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
            response = requests.get(url)

            if response.status_code ==200:
                Pokemon.objects.all().delete()
                data= response.json()
                abilities_set = data.pop('abilities',[])
                moves = data.pop('moves',[])
               # move_set = data.pop('moves',[])
                new_pokemon = Pokemon.objects.create(
                    name = data['name'],
                    types = data['types'],
                    id = data['id'],
                    height = data['height'],
                    weight = data['weight'],
                    #abilities = data['abilities'],
                    #moves = data['moves'],
                    #image_url = data['image_url']
                    )
                
                for ability in abilities_set:
                    ability_name = Abilities.objects.create(name=ability)
                    new_pokemon.abilities.add(ability_name)
                for move in moves:
                    move_name = Moves.objects.create(name=move)
                    new_pokemon.moves.add(move_name)

   


                
            else:
                print(pokemon,"Request failed", response.status_code)
        self.stdout.write(self.style.SUCCESS('Custom command executed successfully'))

            