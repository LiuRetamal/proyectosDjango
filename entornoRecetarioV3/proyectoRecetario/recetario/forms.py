from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre','subnombre','ingredientes', 'imagen', 'receta','author','categorias']
        widgets = {
            'nombre': forms.TextInput(attrs={'style': 'background-color:lightblue'}),
            'subnombre': forms.TextInput(attrs={'style': 'background-color:lightblue','placeholder': 'escribe el subnombre'}),
            # 'ingredientes': forms.Textarea(attrs={'class:btn'}),
        }
        labels={
            'subnombre':'Sub Nombre',
        }