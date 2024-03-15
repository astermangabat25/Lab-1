from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(validators=[MinLengthValidator(255, 'the field must contain at least 255 characters')])

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile, 
        on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete = models.CASCADE,
        related_name = "recipe"
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete = models.CASCADE,
        related_name = "ingredients"
    )


    