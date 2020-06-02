from django.contrib import admin
from .models import Pizza, Toppings, Subs, Pasta, Salads, DinnerPlatters, Orders, OrderItems

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(Orders)
admin.site.register(OrderItems)
