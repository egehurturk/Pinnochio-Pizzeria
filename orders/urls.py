from django.urls import path

from orders import views

urlpatterns = [
    path("", views.index, name="index"),
    path("locate/", views.locate, name="locate"),
    path("menu/", views.menu, name="menu"),
    path("showcart/", views.showcart, name="showcart"),
    path("cart/", views.cart, name="cart"),

]
