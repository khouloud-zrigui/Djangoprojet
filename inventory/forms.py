from django.core import validators 
from django import forms
from.models import User
from.models import Produit

class ClientRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput (attrs={'class': 'form-control'}),
            'password': forms.PasswordInput (render_value= True , attrs={'class': 'form-control'})
        }


class ProduitRegistration(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['name_prod','description','quantite','prix_unit']
        widgets = {
            'name_prod': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'quantite': forms.TextInput(attrs={'class': 'form-control'}),
            'prix_unit':forms.TextInput(attrs={'class': 'form-control'})
        }
