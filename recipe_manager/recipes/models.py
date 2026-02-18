from django.db import models
from storage.models import StorageItem

class Recipe(models.Model):
    name = models.CharField(max_length=127)
    quantity = models.IntegerField()

    items = models.ManyToManyField(
        StorageItem,
        through="RecipeIngredient",
        related_name="recipes",
    )

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    item = models.ForeignKey(StorageItem, on_delete=models.CASCADE)
    used_quantity = models.FloatField()

    def __str__(self):
        return f"{self.recipe.name} - {self.item.name}"