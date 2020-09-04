from django.shortcuts import render
from .models import Pizza, Topping, Sub, Extra, Pasta, Salad, Dinner
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from util import switch
from django.core import serializers

def index(request):
    return render(request, "orders/index.html")


@login_required
def locate(request):
    return render(request, "orders/locate.html")


@login_required
def menu(request):
    context = {
        "regularpizza": Pizza.objects.filter(crust="Regular").all(),
        "sicilianpizza": Pizza.objects.filter(crust="Sicilian").all(),
        "subs": Sub.objects.all(),
        "dinner": Dinner.objects.all(),
        "salads": Salad.objects.all(),
        "Toppings": Topping.objects.all(),
        "Pasta": Pasta.objects.all()
    }
    return render(request, "orders/menu.html", context)


@login_required
def showcart(request):
    product = request.GET['product']
    if request.GET['type'] == "small":
        size = f"{request.GET['type']}_price"
    elif request.GET['type'] == "large":
        size = f"{request.GET['type']}_price"
    else:
        size = "price"

    product_name = product.split("-")[0]
    product_id = product.split("-")[1]

    query = switch(product_name)

    db_list = ["Dinner", "Extra", "Pasta", "Pizza", "Salad", "Sub", "Topping"]


    return JsonResponse(
        {
            "product_name": product_name,
            "product_id": product_id,
            "size": size,
            "queryresult": serializers.serialize('json', [query]),
        }
    )


def menuidview(request):
    context = {
        "subid": Sub.objects.all().values('id'),
        "regpizzaid": Pizza.objects.all().values("id")[:5],
        "sicpizzaid": Pizza.objects.all().values("id")[6:],
        "pastaid": Pasta.objects.all().values("id"),
        "extraid": Extra.objects.all().values("id"),
        "saladid": Salad.objects.all().values("id"),
        "toppingid": Topping.objects.all().values("id"),
        "dinnerid": Dinner.objects.all().values("id")
    }
    return render(request, "orders/id.html", context)




"""
Subs: {id: 28}...{id: 42} / difference: 27
Reg-Pizza: {id: 14}...{id: 18} / difference: 13
Sic-Pizza: {id: 19}...{id: 23} / difference: 18
Pasta: {id: 11}...{id: 13} / difference:10
Extra: {id: 7}...{id: 10} / difference: 6
Toppings: {id: 43}...{id: 61} / difference; 42
Salad: {id: 24}...{id: 27} / difference: 23
Dinner: {id: 1}...{id: 6}  / difference: 0
"""
