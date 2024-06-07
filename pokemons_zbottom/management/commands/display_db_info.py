from django.core.management.base import BaseCommand
from pokemons_zbottom.models import Pokemon


class Command(BaseCommand):
    def handle(self, *args, **options):
        db = Pokemon.objects.all()
        
        for data in db:           
            self.stdout.write(self.style.SUCCESS(f'ID: {data.id}, Name: {data.name} Moves: {", ".join(move.name for move in data.moves.all())}'))


        

        
        
