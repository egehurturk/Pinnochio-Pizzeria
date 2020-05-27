from django.shortcuts import render
from .models import Pizza, Toppings, Subs, Pasta, Salads, DinnerPlatters


# Create your views here.
def index(request):
    context = {
        "Topping":Toppings.objects.all()
    }
    return render(request, "orders/index.html", context)