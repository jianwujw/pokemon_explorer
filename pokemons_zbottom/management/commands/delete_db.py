from django.core.management import BaseCommand
from pokemons_zbottom.models import Pokemon

class Command(BaseCommand):
    def handle(self, *args, **options):
        Pokemon.objects.all().delete()