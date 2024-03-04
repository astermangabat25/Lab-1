from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx={ "recipes":recipes }
    return render(request, 'recipe_list.html', ctx)

def page(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx={ "recipe":recipe }
    return render(request, 'page.html', ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name='recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name='page.html'