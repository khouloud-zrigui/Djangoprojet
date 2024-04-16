from django.core import validators 
from django import forms
from.models import User
from.models import Produit
from.models import Commande

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

class CommandeRegistration(forms.ModelForm):
    client_id = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    produit_id = forms.ModelChoiceField(queryset=Produit.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    commande_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Commande
        fields = ['client_id', 'produit_id', 'quantite_cmd', 'commande_date']
        widgets = {
            'quantite_cmd': forms.TextInput(attrs={'class': 'form-control'}),
        }
