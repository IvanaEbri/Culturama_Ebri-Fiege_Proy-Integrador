from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

#Restricción
class StaffRequiredMixin(LoginRequiredMixin):
    # Verifica si el usuario no está autenticado o no es staff y lo redirige al login con mensaje
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            messages.error(request, "Acceso denegado: No es parte del staff.")  # muestra el mensaje de error
            return redirect(reverse_lazy('home'))  # Redirige al login si no es staff
        return super().dispatch(request, *args, **kwargs)

#Registro de usuarios
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

#Login de usuarios
class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        
        # Redirigir según el tipo de usuario
        if user.is_active:
            if user.is_staff:
                return redirect('SitesAdmin')
            else:
                return redirect('home')
        return redirect('home')

    def form_invalid(self, form):
        messages.error(self.request, "Los datos ingresados son incorrectos. Por favor, inténtalo de nuevo.")
        return super().form_invalid(form)

#Cerar sesión
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

#Confirmar cierre de sesión
class UserConfirmLogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'logout.html'

#vista protegida
class AdminSiteView(StaffRequiredMixin, TemplateView):
    template_name = 'site_adm.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context