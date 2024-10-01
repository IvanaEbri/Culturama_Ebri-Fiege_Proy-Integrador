from django import forms
from .models import Site_tour
from tag.models import Tag

class SiteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Site_tour
        fields = [
            'site_name', 
            'description', 
            'url', 
            'image', 
            'adress', 
            'coordinates', 
            'journey_time', 
            'site_type', 
            'accesibility', 
            'state'
        ]
        labels = {
            'site_name': 'Nombre del sitio',
            'description': 'Descripción',
            'url': 'Enlace',
            'image': 'Imagen',
            'adress': 'Dirección',
            'coordinates': 'Coordenadas',
            'journey_time': 'Tiempo de recorrido',
            'site_type': 'Tipo de sitio',
            'accesibility': 'Accesibilidad',
            'state': 'Estado (Activo)'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'journey_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'site_type': forms.Select(),
            'accesibility': forms.Textarea(attrs={'rows': 2}),
            'state': forms.CheckboxInput(),
        }

class DeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirmar eliminación', required=True, initial=True)