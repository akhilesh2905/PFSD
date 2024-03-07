# recipes/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
