from django import forms
from django.forms import inlineformset_factory

from .models import RecipeIngredient, Recipe, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'
