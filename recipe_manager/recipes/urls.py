from django.urls import path
from .views import RecipesView, RecipeDetailView, RecipeDeleteView, RecipeCreateView, RecipeEditView

urlpatterns = [
    path("", RecipesView.as_view(), name="recipes"),
    path("<int:pk>", RecipeDetailView.as_view(), name="recipe_detail"),
    path("edit/<int:pk>", RecipeEditView, name="recipe_edit"),
    path("delete/<int:pk>", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("create/", RecipeCreateView, name="recipe_create"),
]