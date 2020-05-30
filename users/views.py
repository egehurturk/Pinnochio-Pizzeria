from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    context = {
        "user": request.user,
    }
    return render(request, 'users/login.html', context)


def login_view(request):
    username = request.POST.get("username", False)
    password = request.POST.get("password", False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, f'{username} Welcome Back!')
        return redirect("index")
    else:
        messages.warning(request, f'Invalid credentials')
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return render(request, "orders/index.html", {"message": "Logged Out."})

def signup_view(request):
    pass
