from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from .models import Recipe, RecipeIngredient, StorageItem

# Create your views here.
class RecipesView(ListView):
    model = Recipe
    template_name = 'recipes.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'detail_recipe.html'

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = '/recipes'



def RecipeEditView(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        recipename = request.POST.get('recipe_name')
        recipe.name = recipename
        
        ingredient_ids = request.POST.getlist("ingredient_id")
        quantities = request.POST.getlist("quantity_used")

        for i in range(len(ingredient_ids)):
            ingredient = RecipeIngredient.objects.get(id=ingredient_ids[i])
            ingredient.used_quantity = quantities[i]
            ingredient.save()

        recipe.save()
        return redirect("recipe_detail", pk=pk)
    
    return render(request, "edit_recipe.html", {'recipe' : recipe})



def RecipeCreateView(request):
    if request.method == "POST":
        recipe = Recipe.objects.create(
            name = request.POST.get('recipe_name'),
            quantity = request.POST.get('recipe_quantity')
        )
        
        items_names = request.POST.getlist('item_name[]')
        quantities = request.POST.getlist('quantity[]')

        for i in range(len(items_names)):
            item_name = items_names[i].strip()

            item, created = StorageItem.objects.get_or_create(
                name=item_name,
                defaults={
                    "quantity": None,
                    "price": None,
                }
            )

            RecipeIngredient.objects.create(
                recipe=recipe,
                item=item,
                used_quantity=quantities[i]
            )
        
        return redirect("recipe_detail", pk=recipe.pk)

    storage_items = StorageItem.objects.all()
    return render(request, "create_recipe.html", {'storage_items' : storage_items})