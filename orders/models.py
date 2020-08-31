# author: Ege Hurturk
# Github: https://github.com/egehurturk
# python 3.7
# django 2.3

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Holds the values for categories."""
    PIZZA = 'Pizza'
    TOPPING = 'Topping'
    SUB = 'Sub'
    EXTRA = 'Extra'
    PASTA = 'Pasta'
    SALAD = 'Salad'
    DINNER = 'Dinner Platter'
    CATEGORY_CHOICES = (
        (PIZZA, 'Pizza'),
        (TOPPING, 'Topping'),
        (SUB, 'Sub menu'),
        (EXTRA, 'Extra'),
        (PASTA, 'Pasta'),
        (SALAD, 'Salad'),
        (DINNER, 'Dinner Platter')
    )
    # In order to make custom categories, delete choices attribute.
    name = models.CharField(max_length=16, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"

class Item(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    small_price = models.DecimalField(max_digits=4, decimal_places=2, blank=True,  null=True)
    large_price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.category} [{self.name}-{self.price}]'


class Pizza(Item):
    REGULAR = 'Regular'
    SICILIAN = 'Sicilian'
    PIZZA_CHOICES = (
        (REGULAR, 'Regular'),
        (SICILIAN, 'Sicilian'),
    )
    crust = models.CharField(max_length=30, choices=PIZZA_CHOICES)
    max_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.crust} {self.name} - {self.small_price} {self.large_price}'

class Topping(Item):
    def __str__(self):
        return f"{self.name}"

class Pasta(Item):
    def __str__(self):
        return f"{self.name}"

class Salad(Item):
    def __str__(self):
        return f"{self.name}"

class Dinner(Item):
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Dinner Platters'
        verbose_name = 'Dinner Platter'

class Extra(Item):
    def __str__(self):
        return f'{self.name}'

class Sub(Item):

    def __str__(self):
        return f'{self.name}'
