from django.db import models


# Create your models here.
class Abilities(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Moves(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=30)  
    id = models.PositiveIntegerField(primary_key=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    abilities = models.ManyToManyField(Abilities)
    moves = models.ManyToManyField(Moves)
    image_url = models.URLField(blank=True)
