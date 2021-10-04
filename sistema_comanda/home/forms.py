from django import forms
from .models import bebida, comida

class bebidaForm(forms.ModelForm):
    class Meta:
        model = bebida
        fields = ['produto', 'preco']

class comidaForm(forms.ModelForm):
    class Meta:
        model = bebida
        fields = ['produto', 'preco']