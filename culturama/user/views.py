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
from tag.models import Tag, Site_tag
from site_tour.models import Site_tour 
import random

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
                return redirect('HomeUser')
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

#vista selección de etiqueta/temática
class Route1View(LoginRequiredMixin, TemplateView):
    template_name = 'route1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()  # mostrar tags en plantillla
        return context

    def post(self, request, *args, **kwargs):
        selected_tag_id = request.POST.get('tag_id')  # Obtener id de la etiqueta seleccionada

        if selected_tag_id:
            return redirect('Route2', tag_id=selected_tag_id)  # Redirigir a Route2 con el ID de la etiqueta elegida
        
        return self.get(request, *args, **kwargs)  # Si no hay selección, vuelve a cargar el formulario

#vista cantidad de paradas
class Route2View(LoginRequiredMixin, TemplateView):
    template_name = 'route2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        context['tag'] = Tag.objects.get(id_tag=tag_id)
        context['sitios'] = Site_tag.objects.filter(tag=context['tag']).values_list('site_tour', flat=True)
        context['site_options'] = [1, 2, 3, 4]
        return context

    def post(self, request, *args, **kwargs):
        selected_tag_id = self.kwargs.get('tag_id')  # Obtener id de la etiqueta seleccionada
        selected_cant_paradas = request.POST.get('sites') 

        if selected_cant_paradas:
            return redirect('Answer', tag_id=selected_tag_id, cant_paradas=selected_cant_paradas)  
        
        return self.get(request, *args, **kwargs)  # Si no hay selección, vuelve a cargar el formulario

    # def post(self, request, *args, **kwargs):
    #     tag_id = request.POST.get('tag_id')
    #     paradas = request.POST.get('paradas')
    #     sitios = list(Site_tag.objects.filter(tag__id_tag=tag_id).values_list('site_tour', flat=True))

    #     # si el user elige aleatoriamenet
    #     if paradas == 'random':
    #         num_paradas = random.randint(1, min(4, len(sitios)))  # numero entre 1 y 4
    #     else:
    #         num_paradas = int(paradas)
    #     return redirect('Answer', tag_id=tag_id, cant_paradas=num_paradas)


class AnswerView(LoginRequiredMixin, TemplateView):
    template_name = 'answer.html'

    def paradas (self,cant_paradas):
     # Convertir num_paradas a entero
        if cant_paradas == 'random':
            num_paradas = random.randint(1, 4)  
        else:
            num_paradas = int(cant_paradas)  # Convertir a entero si no es 'random'
        return num_paradas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        cant_paradas = self.kwargs['cant_paradas']
        context['tag'] = Tag.objects.get(id_tag=tag_id)
        site_tags = Site_tag.objects.filter(tag=tag_id).values_list('site_tour', flat=True)
        sitios = Site_tour.objects.filter(id_site_tour__in=site_tags, state=True)  # Filtrar solo los activos
        num_paradas = self.paradas(cant_paradas)
        lugares = list(sitios)
        context['lugares_seleccionados'] = random.sample(lugares, k=min(num_paradas, len(lugares)))
        num_paradas = len(context['lugares_seleccionados'])
        context['num_paradas'] = num_paradas

        return context

    # def post(self, request, *args, **kwargs):
    #     tag_id =  self.kwargs.get('tag_id') 
    #     cant_paradas = self.kwargs.get('cant_paradas')
    #     num_paradas = self.paradas(cant_paradas)
    #     tag = Tag.objects.get(id_tag=tag_id)

    #     site_tag = Site_tag.objects.filter(tag=tag).values_list('site_tour', flat=True)
    #     lugares = Site_tour.objects.filter(id__in=site_tag)

    #     lugares_seleccionados = random.sample(list(lugares), k=min(1, len(lugares)))
    #     context = {
    #         'lugares': lugares,
    #         'num_paradas': len(lugares_seleccionados),
    #         'lugares': lugares_seleccionados,
    #         'tag': tag
    #     }
    #     return render(request, self.template_name, context)

def map_view(request):
    return render(request, 'map.html')