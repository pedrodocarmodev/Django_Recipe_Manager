from django.shortcuts import render, get_object_or_404
from recipes.models import Recipe, RecipeIngredient

def CalculatorView(request):
    recipes = Recipe.objects.all()

    return render(request, "calculator.html", {"recipes": recipes})


def RecipePriceView(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    data = {
        "recipe" : recipe.name,
        "items" : []
    }


    ingredients = RecipeIngredient.objects.filter(recipe=recipe).select_related("item")


    for ingredient in ingredients:

        storage_item = ingredient.item

        data["items"].append({
            "name": storage_item.name,
            "required_quantity": ingredient.used_quantity,  
            "price_per_kg": storage_item.price,             
            "available_quantity": storage_item.quantity    
        })

    return render(request, 'recipe_price.html', data)