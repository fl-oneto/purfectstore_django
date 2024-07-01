from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignUpForm, FormularioContacto, CustomAuthenticationForm
from django.contrib import messages
from .models import Producto, Categoria




# Create your views here


def home(request):
    
    return render(request, 'landing.html')


def contacto(request):
    success = False
    form = FormularioContacto()
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            success = True
            form = None
            return render(request, 'contacto.html', {'form': form, 'success': success})
    return render(request, 'contacto.html', {'form': form, 'success': success})

def nosotros(request):
    
    return render(request, 'nosotros.html')


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


def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if 'carrito' not in request.session:
        request.session['carrito'] = {}
    carrito = request.session['carrito']
    if producto_id in carrito:
        carrito[producto_id]['cantidad'] += 1
    else:
        print("Producto imagen URL:", producto.imagen.url)
        carrito[producto_id] = {
            'id': producto.id,
            'imagen': producto.imagen.url,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'cantidad': 1,
        }
    request.session.modified = True  
    return redirect('productosAseo')

def micuenta(request):
    return render(request, 'micuenta.html', {'user': request.user})  

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    return render(request, 'carrito.html', {'carrito': carrito})







