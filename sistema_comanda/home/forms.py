from django import forms
from .models import bebida, comida, usuario

class bebidaForm(forms.ModelForm):
    class Meta:
        model = bebida
        fields = ['produto', 'preco']

class comidaForm(forms.ModelForm):
    class Meta:
        model = comida
        fields = ['produto', 'preco']




'''   class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nome', 'num', 'gasto']   '''