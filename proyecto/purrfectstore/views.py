from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages


# Create your views here


def home(request):
    
    return render(request, 'landing.html')

def carrito(request):
    
    return render(request, 'carrito.html')

def contacto(request):
    
    return render(request, 'contacto.html')

def nosotros(request):
    
    return render(request, 'nosotros.html')

def productosAseo(request):
    
    return render(request, 'productosAseo.html')

def micuenta(request):
    
    return render(request, 'micuenta.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos. Por favor, intenta de nuevo.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

