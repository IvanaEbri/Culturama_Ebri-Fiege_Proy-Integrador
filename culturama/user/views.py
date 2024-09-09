from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class UserRegisterView (CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def form_valid(self, form):
        # Procesar el formulario si es válido
        user = form.save(commit=False)
        # Podemos hacer algo
        user.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Agregar mensajes de error a la lista de mensajes
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return super().form_invalid(form)

class UserLoginView (LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        
        # Redirigir según el tipo de usuario
        if user.is_active:
            return redirect('home')
        #     if user.cliente:
        #         return redirect('home')
        #     else:
        #         return redirect('home_admin')
        # else:
        #     return redirect('home')

    def form_invalid(self, form):
        messages.error(
            self.request, "Los datos ingresados son incorrectos. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        return super().form_invalid(form)

class UserLogoutView (LogoutView):
    next_page = reverse_lazy('home')  # Redirige a la página principal después del logout

class UserConfirmLogoutView (LoginRequiredMixin, View):
    template_name = 'logout.html'