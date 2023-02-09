from django import forms
from .models import Camiones

class CamionesForm(forms.ModelForm):
    class Meta:
        model = Camiones
        fields = ['marca','modelo','imagen','descripcion', 'kilometros','precio', 'author', 'categorias']
        widgets = {
            'marca': forms.TextInput(attrs={'style': 'background-color:lightblue','placeholder': 'escribe la marca'}),
            'modelo': forms.TextInput(attrs={'style': 'background-color:lightblue','placeholder': 'escribe el modelo'}),
            'kilometros': forms.TextInput(attrs={'style': 'background-color:lightblue','placeholder': 'escribe los kilometros'}),
            'precio': forms.TextInput(attrs={'style': 'background-color:lightblue','placeholder': 'escribe el precio'}),
            'descripcion': forms.Textarea(attrs={'style': 'background-color:lightblue','placeholder': 'escribe una descripcion del producto'}),
        }