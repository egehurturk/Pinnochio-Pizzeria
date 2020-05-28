from django.shortcuts import render
from .models import Pizza, Toppings, Subs, Pasta, Salads, DinnerPlatters


# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def locate(request):
    return render(request, "orders/locate.html")