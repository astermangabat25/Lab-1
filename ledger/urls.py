from django.urls import path
from .views import recipe_list, page1, page2

urlpatterns = [
    path('recipes/list', recipe_list, name="listahan"),
    path('recipe/1', page1, name="una"),
    path('recipe/2', page2, name="pangalawa"),
]

app_name = 'recipe book'