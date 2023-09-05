from django.core.management.base import BaseCommand
from pokemons_zbottom.models import *
import requests
import time
import sqlite3

class Command(BaseCommand):
    def handle(self, *args, **options):
        pokemon_count = 1281
        Pokemon.objects.all().delete()
        for pokemon in range(1,pokemon_count):
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
            response = requests.get(url)           
            if response.status_code ==200:              
                data= response.json()
                
               # move_set = data.pop('moves',[])
                new_pokemon = Pokemon.objects.create(
                    name = data['name'],
                    #types = data['types'][0]['type']['name'],
                    id = data['id'],
                    height = data['height'],
                    weight = data['weight'],
                    image_url = data['sprites']['front_default']
                    )
                moves = data['moves']
                abilities_set = data['abilities']
                self.stdout.write(data['types'][0]['type']['name'])
                types = data['types']

                for type in types:
                    new_pokemon.types.add(Type.objects.create(name = type['type']['name']))
                    new_pokemon.save()
                    

                for ability in abilities_set:                   
                    ability_name = ability['ability']['name']
                    new_pokemon.abilities.add(Abilities.objects.create(name=ability_name))
                    new_pokemon.save()
                for move in moves:
                    move_name = move['move']['name']
                    new_pokemon.moves.add(Moves.objects.create(name=move_name))
                    self.stdout.write(move_name)
                    new_pokemon.save()


                self.stdout.write(self.style.SUCCESS(f'ID: {new_pokemon.id} Name: {new_pokemon.name} added. Types: {", ".join(type.name for type in new_pokemon.types.all())}'))

               
            else:
                print(pokemon,"Request failed", response.status_code)
        self.stdout.write(self.style.SUCCESS('Custom command executed successfully'))

            