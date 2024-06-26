from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', required=True,
                                max_length=50, min_length=5,
                                error_messages={
                                    'required': 'El usuario es obligatorio',
                                    'max_length': 'El usuario no puede superar los 50 caracteres',
                                    'min_length': 'El usuario debe tener al menos 5 caracteres'
                                },
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Ingrese su usuario',
                                    'class': 'form-control'
                                })
                                )
    password = forms.CharField(label='Contraseña', required=True,
                                max_length=50, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 50 caracteres',
                                    'min_length': 'La contraseña debe tener al menos 1 caracter'
                                },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico', required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}))
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Contraseña'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("El email ya está registrado.")
        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class FormularioContacto(forms.Form):
    email = forms.EmailField(label="Email", max_length=100,min_length=5, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Ingrese su Email', 'class': 'form-control'}),
                            error_messages={'required':'El Email es obligatorio', 'max_length':'el email no puede tener más de 100 caracteres','min_length': 'El email debe tener al menos 5 caracteres'})
    nombre = forms.CharField(label="Nombre", max_length=50, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Ingrese su Nombre', 'class': 'form-control'}),
                            error_messages={'required':'El nombre es obligatorio', 'max_length': 'el nombre no puede tener más de 50 caracteres'})
    
    telefono = forms.CharField(label='Teléfono', max_length=9, min_length=9, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Ingrese su Teléfono', 'class': 'form-control'}),
                            error_messages={'required':'El Teléfono es obligatorio', 'max_length': 'El número de teléfono debe tener 9 digitos', 'min_length': 'El número de teléfono debe tener 9 digitos'})
    mensaje = forms.CharField(label ='Mensaje', max_length=1000, required = True,
                            widget=forms.Textarea(attrs={'placeholder':'Ingrese su mensaje', 'class':'form-control'}),
                            error_messages= {'required':'El mensaje es obligatorio', 'max_length':'El maximo de caracteres es de 1000'})
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise forms.ValidationError('El número de teléfono debe contener solo dígitos.')
        return telefono