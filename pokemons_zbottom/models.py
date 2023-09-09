from django.db import models

class MovesMethod(models.Model):
    name = models.CharField(max_length=100)

class Moves(models.Model):
    name = models.CharField(max_length=100)
    level_learned = models.PositiveIntegerField(default=0)
    move_learn_method = models.ForeignKey(MovesMethod,null=True, on_delete=models.SET_NULL,blank=True)


# Create your models here.
class Abilities(models.Model):
    name = models.CharField(max_length=100)

class Type(models.Model):
    name = models.CharField(max_length=100)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    types = models.ManyToManyField(Type)  
    id = models.PositiveIntegerField(primary_key=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    abilities = models.ManyToManyField(Abilities)
    moves = models.ManyToManyField(Moves)
    image_url = models.URLField(blank=True)


 
