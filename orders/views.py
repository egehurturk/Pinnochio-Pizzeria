from django.shortcuts import render
from .models import Pizza, Toppings, Subs, Pasta, Salads, DinnerPlatters, Orders, OrderItems
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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


@login_required
def showcart(request):
    product = request.GET['product']  # :variable = subs-2 (the second product of subs in the menu)
    size = 'No'  # :variable =  large / small / false (for pasta and salad)
    if request.GET["type"] == 'small':
        size = 'small_price'
    if request.GET['type'] == 'large':
        size = 'large_price'

    product_name = product.split('-')[0]  # :variable = pasta / subs / regular ...
    product_id = product.split('-')[1]  # :variable = 1 / 2 / ...
    print(product, size, product_name, product_id)