from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserCreationForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=20)
    first_name = forms.CharField(label="Nombre", max_length=20)
    last_name = forms.CharField(label="Apellido", max_length=20)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput)
    is_staff = forms.BooleanField(label="Administrador", required=False)

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','is_staff' ,'password1', 'password2']
        labels = {
            'username': 'Username',
            'password1': 'Contraseña',
            'password2': 'Confirme su contraseña',
            'is_staff': 'Administrador',
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields