from django.db import models

# Create your models here.

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

    name = models.CharField(max_length=20)

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
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.small_price} {self.large}"

    class Meta:
        verbose_name = "Dinner platters"
        verbose_name_plural = "Dinner platters"


