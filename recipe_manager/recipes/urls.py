from django.urls import path
from .views import AddRecipeItemView, DeleteRecipeItemView, RecipesView, RecipeDetailView, RecipeDeleteView, RecipeCreateView, UpdateRecipeItemView

urlpatterns = [
    path("", RecipesView.as_view(), name="recipes"),
    path("<int:pk>", RecipeDetailView.as_view(), name="recipe_detail"),
    path("delete/<int:pk>", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("create/", RecipeCreateView, name="recipe_create"),
    path("<int:recipe_id>/add-item/", AddRecipeItemView, name="add_recipe_item"),
    path("ingredient/<int:id>/edit/", UpdateRecipeItemView, name="update_recipe_item"),
    path("ingredient/<int:id>/delete/", DeleteRecipeItemView, name="remove_recipe_item")
]