from django.core.management.base import BaseCommand
from pokemons_zbottom import *
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        pokemon_count = 1281
        for pokemon in range(1,pokemon_count):
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
            response = requests.get(url)

            if response.status_code ==200:
                data= response.json()
                #Pokemon.objects.create(**data)
                
                print(data['name'])
            else:
                print("Request failed", response.status_code)
        self.stdout.write(self.style.SUCCESS('Custom command executed successfully'))

            