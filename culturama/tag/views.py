from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .models import Tag
from .forms import TagForm
from django.contrib import messages
from site_tour.views import StaffRequiredMixin

# vista praa crear una nueva etiqueta
class CreateTagView(StaffRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_new.html'  
    success_url = reverse_lazy('SitesAdmin')
    
    def form_valid(self, form):
        messages.success(self.request, 'Etiqueta creada exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al crear la etiqueta.')
        return super().form_invalid(form)

# vista para editar una etiqueta
class TagEditView(StaffRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_edit.html'
    success_url = reverse_lazy('SitesAdmin')
    
    def form_valid(self, form):
        messages.success(self.request, 'Etiqueta editada exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al editar la etiqueta.')
        return super().form_invalid(form)

# vista para listar las etiquetas
class TagSeeView(StaffRequiredMixin,TemplateView):
    model = Tag
    template_name = 'tag_see.html'
    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(pk=kwargs['pk'])
        return context
