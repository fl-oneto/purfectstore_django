"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from purrfectstore.views import home, contacto, nosotros, productosAseo, productosCamas, productosJuguetes, productosRopa, ver_carrito, micuenta, obt_img_gato
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('purrfectstore/', include('purrfectstore.urls')),
    path('carrito/', ver_carrito, name="carrito"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"), 
    path('api/cat-images/', obt_img_gato, name='obt_img_gato'),
    path('productosAseo/', productosAseo, name="productosAseo"),
    path('productosCamas/', productosCamas, name='productosCamas'),
    path('productosJuguetes/', productosJuguetes, name='productosJuguetes'),
    path('productosRopa/', productosRopa, name='productosRopa'),
    path('micuenta/', micuenta, name="micuenta"),  # NO RETIRAR PLSPLS, esencial para el deploy 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)