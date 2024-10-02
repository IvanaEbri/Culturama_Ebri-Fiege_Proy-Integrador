from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Site_tour
from .forms import SiteForm, DeleteForm
from user.views import StaffRequiredMixin
from tag.models import Tag 

def home(request):
    return render(request, 'home.html')

# vista de administración de sitios
class SitesAdminView(StaffRequiredMixin, TemplateView):
    template_name = 'site_adm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites_tour'] = Site_tour.objects.all()
        context['tags'] = Tag.objects.all()
        return context
    
# craer un nuevo sitio
class CreateSiteView(StaffRequiredMixin, CreateView):
    model = Site_tour
    form_class = SiteForm
    template_name = 'site_new_edit.html'
    success_url = reverse_lazy('SitesAdmin')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)

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
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)

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
        context['site'] = Site_tour.objects.get(pk=kwargs['pk'])
        return context
