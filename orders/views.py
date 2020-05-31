from django.shortcuts import render
from .models import Pizza, Toppings, Subs, Pasta, Salads, DinnerPlatters
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, "orders/index.html")


@login_required
def locate(request):
    return render(request, "orders/locate.html")


@login_required
def menu(request):
    context = {
        "regularpizza": Pizza.objects.filter(type="Regular").all(),
        "sicilianpizza": Pizza.objects.filter(type="Sicilian").all(),
        "subs": Subs.objects.all(),
        "dinner": DinnerPlatters.objects.all(),
        "salads": Salads.objects.all(),
        "Toppings": Toppings.objects.all(),
        "Pasta": Pasta.objects.all()
    }
    return render(request, "orders/menu.html", context)
