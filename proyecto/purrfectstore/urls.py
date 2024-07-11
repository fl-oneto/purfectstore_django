from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('home/', views.home, name='home'),
    path('custom_login/', views.custom_login, name='custom_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('productosAseo/', views.productosAseo, name='productosAseo'),
    path('contacto/', views.contacto, name='contacto'),
    #path('micuenta/', views.micuenta, name='micuenta'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]
