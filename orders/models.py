# author: Ege Hurturk
# Github: https://github.com/egehurturk
# python 3.7
# django 2.3

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Choices - Toppings
PEPPERONI = 'Pepperoni'
SAUSAGE = 'Sausage'
MUSHROOMS = 'Mushrooms'
ONIONS = 'Onions'
HAM = 'Ham'
CANADIAN_BACON = 'Canadian Bacon'
PINEAPPLE = 'Pineapple'
EGGPLANT = 'Eggplant'
TOMATO_BASIL = 'Tomato & Basil'
GREEN_PEPPERS = 'Green Peppers'
HAMBURGER = 'Hamburger'
SPINACH = 'Spinach'
ARTICHOKE = 'Artichoke'
BUFFALO_CHICKEN = 'Buffalo Chicken'
BARBECUE_CHICKEN = 'Barbecue Chicken'
ANCHOVIES = 'Anchovies'
BLACK_OLIVES = 'Black Olives'
FRESH_GARLIC = 'Fresh Garlic'
ZUCCHINI = 'Zucchini'

TOPPINGS_CHOICES = [
    (PEPPERONI, 'Pepperoni'),
    (SAUSAGE, 'Sausage'),
    (MUSHROOMS, 'Mushrooms'),
    (ONIONS, 'Onions'),
    (HAM, 'Ham'),
    (CANADIAN_BACON, 'Canadian Bacon'),
    (PINEAPPLE, 'Pineapple'),
    (EGGPLANT, 'Eggplant'),
    (TOMATO_BASIL, 'Tomato & Basil'),
    (GREEN_PEPPERS, 'Green Peppers'),
    (HAMBURGER, 'Hamburger'),
    (SPINACH, 'Spinach'),
    (ARTICHOKE, 'Artichoke'),
    (BUFFALO_CHICKEN, 'Buffalo Chicken'),
    (BARBECUE_CHICKEN, 'Barbecue Chicken'),
    (ANCHOVIES, 'Anchovies'),
    (BLACK_OLIVES, 'Black Olives'),
    (FRESH_GARLIC, 'Fresh Garlic'),
    (ZUCCHINI, 'Zucchini'),
]


# Choices - Product Types
REGULAR_PIZZA = 'Regular Pizza'
SICILIAN_PIZZA = 'Sicilian Pizza'
# TOPPINGS = 'Toppings'
SUBS = 'Subs'
PASTA = 'Pasta'
SALADS = 'Salads'
DINNER_PLATTERS = 'Dinner Platters'

PRODUCT_TYPE_CHOICES = [
    (REGULAR_PIZZA, 'Regular Pizza'),
    (SICILIAN_PIZZA, 'Sicilian Pizza'),
    # (TOPPINGS, 'Toppings'),
    (SUBS, 'Subs'),
    (PASTA, 'Pasta'),
    (SALADS, 'Salads'),
    (DINNER_PLATTERS, 'Dinner Platters'),
]


class Pizza(models.Model):
    """ Defines the pizza class (2 types: Regular, Sicilian) (Required fields: name, type, prices) """

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=25)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.type} {self.small_price} {self.large_price}"

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"


class Toppings(models.Model):
    """ Defines the toppings (Required fields: name) """

    name = models.CharField(choices=TOPPINGS_CHOICES, max_length=30)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Toppings"
        verbose_name_plural = "Toppings"


class Subs(models.Model):
    """ Defines subs in the menu. (Required fields: name, prices) """

    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.small_price} {self.large_price}"

    class Meta:
        verbose_name = "Subs"
        verbose_name_plural = "Subs"


class Pasta(models.Model):
    """ Defines pastas in the menus (Required fields: name, price) """

    name = models.CharField(max_length=35)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "Pasta"
        verbose_name_plural = "Pastas"


class Salads(models.Model):
    """ Defines salads in the menu (Required Fields: name, price) """

    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}, {self.price}"

    class Meta:
        verbose_name = "Salads"
        verbose_name_plural = "Salads"


class DinnerPlatters(models.Model):
    """ Defines the dinner platters in the menu """

    name = models.CharField(max_length=25)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.small_price} {self.large_price}"

    class Meta:
        verbose_name = "Dinner platters"
        verbose_name_plural = "Dinner platters"


class Orders(models.Model):
    """ Contains Customer ID (Foreign Key to the User Model), Order Status (Pending, ...) """

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer', default=None)
    order_status = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.customer} - {self.order_status}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class OrderItems(models.Model):
    """ The items in the order (One Order can contain multiple OrderItems, one user can contain multiple Orders) """

    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="order")  # blank = False
    product_type = models.CharField(max_length=50, choices=PRODUCT_TYPE_CHOICES)                            # blank = False
    product_size = models.CharField(max_length=50)                            # blank = True
    quantity = models.IntegerField()                                          # blank = False ?
    cost = models.DecimalField(default=0,max_digits=4, decimal_places=2)                                     # blank = False ?
    toppings_1 = models.CharField(max_length=30, choices=TOPPINGS_CHOICES, default=None, blank=True)    # blank = True
    toppings_2 = models.CharField(max_length=30, choices=TOPPINGS_CHOICES, default=None, blank=True) 
    toppings_3 = models.CharField(max_length=30, choices=TOPPINGS_CHOICES, default=None, blank=True) 
    toppings_4 = models.CharField(max_length=30, choices=TOPPINGS_CHOICES, default=None, blank=True)   


    def __str__(self):
        return \
        f'''
        Order No {self.order}, {self.product_size}, {self.product_type}, {self.quantity}, {self.cost}, {self.toppings_1}, {self.toppings_2}, {self.toppings_3}, {self.toppings_4}
        '''

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'


# FIXME: In Product type choices, there aren't a choice for Pizza types

''' 
IMPORTANT QUESTIONS TO ASK:
    - How can a user place an order?
    - How can a user select toppings?
    - How can a user select extras for subs?
    - When should I create Order model?
    
'''

# PROBLEMS: AUTO ADD THE USER (CURRENT LOGGED IN USER) TO THE ORDERS
#           ---------  3/06/2020  ------------


