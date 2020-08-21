from django.contrib import admin
from .models import *

# Category
admin.site.register(Category)

# Menu
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Extra)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner)