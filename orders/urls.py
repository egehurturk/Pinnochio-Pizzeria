from django.urls import path

from orders import views

urlpatterns = [
    path("", views.index, name="index"),
    path("locate/", views.locate, name="locate"),
    path("menu/", views.menu, name="menu"),

]
