from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag'] 
        labels = {
            'tag': 'Nombre de la Etiqueta'
        }
        widgets = {
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
        }
