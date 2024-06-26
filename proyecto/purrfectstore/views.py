from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignUpForm, FormularioContacto, CustomAuthenticationForm
from django.contrib import messages
from .models import Producto, Categoria


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
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print('login exitoso')
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})  

def productosAseo(request):
    categoria_aseo = get_object_or_404(Categoria, nombre='Aseo e Higiene')
    productos = Producto.objects.filter(categoria=categoria_aseo, disponible=True)
    print(productos)
    return render(request, 'productosAseo.html', {'productos': productos, 'categoria': categoria_aseo})

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']

            # Aquí puedes procesar los datos como necesites (guardar en la base de datos, enviar por correo, etc.)

            # Redirigir a una página de éxito o mostrar un mensaje de éxito
            return render(request, 'success.html', {'nombre': nombre, 'email': email, 'telefono': telefono, 'mensaje': mensaje})
    else:
        form = FormularioContacto()

    # Renderizar el formulario inicialmente o en caso de errores
    return render(request, 'contacto.html', {'form': form})