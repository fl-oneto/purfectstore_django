from django.shortcuts import render

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