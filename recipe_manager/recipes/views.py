from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from .models import Recipe, RecipeIngredient, StorageItem

# Create your views here.
class RecipesView(ListView):
    model = Recipe
    template_name = 'recipes.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'detail_recipe.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = StorageItem.objects.all().order_by("name")
        return context

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = '/recipes'


def RecipeCreateView(request):
    if request.method == "POST":
        name = request.POST.get("recipe_name")
        quantity = request.POST.get("recipe_quantity")

        recipe = Recipe.objects.create(
            name=name,
            quantity=quantity
        )

        item_ids = request.POST.getlist("item_id[]")
        quantities = request.POST.getlist("quantity[]")

        for item_id, qty in zip(item_ids, quantities):
            RecipeIngredient.objects.create(
                recipe=recipe,
                item_id=item_id,
                used_quantity=qty
            )

        return redirect("recipe_detail", pk=recipe.id)

    storage_items = StorageItem.objects.all().order_by("name")
    return render(request, "create_recipe.html", {"storage_items": storage_items})



def AddRecipeItemView(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=recipe_id)
        item_id = request.POST.get("item_id")
        quantity = request.POST.get("used_quantity")

        RecipeIngredient.objects.create(
            recipe=recipe,
            item=item_id,
            used_quantity=quantity
        )

    return redirect("recipe_detail", pk=recipe_id)


def UpdateRecipeItemView(request, id):
    ingredient = get_object_or_404(RecipeIngredient, id=id)

    if request.method == "POST":
        ingredient.used_quantity = request.POST.get("used_quantity")
        ingredient.save()

    return redirect("recipe_detail", pk=ingredient.recipe.id)


def DeleteRecipeItemView(request, id):
    ingredient = get_object_or_404(RecipeIngredient, id=id)
    recipe_id = ingredient.recipe.id
    ingredient.delete()

    return redirect("recipe_detail", pk=recipe_id)