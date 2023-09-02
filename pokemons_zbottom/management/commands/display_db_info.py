from django.core.management.base import BaseCommand
import sqlite3
from pokemons_zbottom.models import Pokemon
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        db = Pokemon.objects.all()

        for items in db:
            print(items)
        self.stdout.write(self.style.SUCCESS('Custom command executed successfully'))