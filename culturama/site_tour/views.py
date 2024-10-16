from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Site_tour
from .forms import SiteForm, DeleteForm
from user.views import StaffRequiredMixin
from tag.models import Site_tag, Tag

def home(request):
    return render(request, 'home.html')

# vista de administración de sitios
class SitesAdminView(StaffRequiredMixin, TemplateView):
    template_name = 'site_adm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#context['sites_tour'] = Site_tour.objects.all()
        context['sites_tour'] = Site_tour.objects.all().prefetch_related('site_tag_set__tag')
        #context['sites_tag'] = Site_tag.objects.all() 
        context['tags'] = Tag.objects.all()
        return context
    
# craer un nuevo sitio
class CreateSiteView(StaffRequiredMixin, CreateView):
    model = Site_tour
    form_class = SiteForm
    template_name = 'site_new_edit.html'
    success_url = reverse_lazy('SitesAdmin')

    def form_valid(self, form):
        site_new = form.save(commit=False)
        site_new.save()
        response = super().form_valid(form)
        
        tags = form.cleaned_data['tags']
        for tag in tags:
            Site_tag.objects.create(site_tour=site_new, tag=tag)
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return super().form_invalid(form)

# editar un sitio
class EditSiteView(StaffRequiredMixin, UpdateView):
    model = Site_tour
    form_class = SiteForm
    template_name = 'site_new_edit.html'
    success_url = reverse_lazy('SitesAdmin')

    def form_valid(self, form):
        site_edit = form.save(commit=False)
        site_edit.save()
        response = super().form_valid(form)
        
        # Eliminar todas las etiquetas previas
        Site_tag.objects.filter(site_tour=self.object).delete()
        # Añadir las nuevas etiquetas
        tags = form.cleaned_data['tags']
        for tag in tags:
            Site_tag.objects.create(site_tour=self.object, tag=tag)
        
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return super().form_invalid(form)

# desactivar un sitio
class DeleteSiteView(StaffRequiredMixin, DeleteView):
    model = Site_tour
    form_class = DeleteForm
    template_name = 'site_del.html'
    success_url = reverse_lazy('SitesAdmin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = False
        self.object.save()
        messages.success(request, 'El sitio se ha inactivado.')
        return redirect(self.success_url)

# detalles de un sitio
class SeeSiteAdminView(StaffRequiredMixin, TemplateView):
    template_name = 'site_see_adm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_one = Site_tour.objects.get(pk=kwargs['pk'])
        context['site'] = site_one
        context['site_tag'] = Site_tag.objects.filter(site_tour=site_one)
        return context
