from django.urls import path
from .views import RecipePriceView, CalculatorView

urlpatterns = [
    path("<int:id>", RecipePriceView, name="recipe_price"),
    path("", CalculatorView, name="calculator"),
]