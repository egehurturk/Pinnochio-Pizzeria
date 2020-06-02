from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm
from orders.models import Orders

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
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect("index")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("login")

    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
