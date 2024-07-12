from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Decorador para el login
from .forms import SignUpForm, FormularioContacto, CustomAuthenticationForm, UserProfileForm
from .models import Producto, Categoria, UserProfile
import requests




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

def productosCamas(request):
    return render(request, 'productos_camas.html')

def productosJuguetes(request):
    return render(request, 'productos_juguetes.html')

def productosRopa(request):
    return render(request, 'productos_ropa.html')


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
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales inválidas, por favor intente de nuevo.')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
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

@login_required
def micuenta(request):
    user = request.user
    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            # Verificar si el correo ya existe en la base de datos
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                form.add_error('email', 'Este correo electrónico ya está en uso.')
            else:
                # Actualizar User model
                user.email = email
                user.save()

                # Actualizar UserProfile model
                user_profile.full_name = form.cleaned_data['full_name']
                user_profile.phone = form.cleaned_data['phone']
                user_profile.website = form.cleaned_data['website']
                user_profile.street = form.cleaned_data['street']
                user_profile.city = form.cleaned_data['city']
                user_profile.state = form.cleaned_data['state']
                user_profile.zip_code = form.cleaned_data['zip_code']
                user_profile.save()

                messages.success(request, 'Perfil actualizado correctamente.')
                return redirect('micuenta')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
            print("Formulario no válido")
            print(form.errors)  # Para depuración
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'micuenta.html', {'form': form, 'user': user})








def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total_precio = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito.html', {'carrito': carrito, 'total_precio': total_precio})


# No eliminar,,, grasias owo
'''
@login_required
def editar_perfil(request):
    user = request.user
    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            # Actualizar User model
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.is_staff = form.cleaned_data['is_staff']
            user.save()

            # Actualizar UserProfile model
            user_profile.full_name = form.cleaned_data['full_name']
            user_profile.phone = form.cleaned_data['phone']
            user_profile.website = form.cleaned_data['website']
            user_profile.street = form.cleaned_data['street']
            user_profile.city = form.cleaned_data['city']
            user_profile.state = form.cleaned_data['state']
            user_profile.zip_code = form.cleaned_data['zip_code']
            user_profile.save()

            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('micuenta')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
            print(form.errors)  # Imprime errores de formulario para depuración
    else:
        form = UserProfileForm(instance=user_profile, initial={
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
        })

    return render(request, 'micuenta.html', {'form': form}) '''


def obt_img_gato(request):
    if 'cat_images' in request.session:
        cat_images = request.session['cat_images']
    else:
        response = requests.get("https://api.thecatapi.com/v1/images/search?limit=3")
        data = response.json()
        request.session['cat_images'] = data
        cat_images = data
    return JsonResponse(cat_images, safe=False)