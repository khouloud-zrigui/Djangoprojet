from django.shortcuts import render, HttpResponseRedirect
from .forms import ClientRegistration
from .models import User
from .models import Produit
from .forms import ProduitRegistration

# Create your views here.
#Cette fonction permet d'ajouter et d'afficher un client user
def add_get_client(request):
    if request.method == 'POST':
        fm = ClientRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm , email = em , password = pw )
            reg.save()
            fm = ClientRegistration()
            #cli = User.objects.all()
    else:
        fm = ClientRegistration()    
    cli = User.objects.all()
    return render(request,'inventory/add_show_client.html',{'form':fm, 'clit':cli})

#cette fonction permet de supprimer les données client par id
def delete_client(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')
    
#Cette fonction permet de modifier les informations client
def update_client(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk = id)
        fm = ClientRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk =id)
        fm = ClientRegistration(instance=pi)
                
    return render(request, 'inventory/update_client.html',{'form':fm})
    
#Cette fonction permet d'ajouter et d'afficher un produit
def add_get_produit(request):
    if request.method == 'POST':
        fm = ProduitRegistration(request.POST)
        if fm.is_valid():
            np = fm.cleaned_data['name_prod']
            ds = fm.cleaned_data['description']
            qt = fm.cleaned_data['quantite']
            pu = fm.cleaned_data['prix_unit']
            reg = Produit(name_prod = np , description = ds , quantite = qt , prix_unit = pu )
            reg.save()
            fm = ProduitRegistration()
            
    else:
        fm = ProduitRegistration()   
    prod = Produit.objects.all()
    return render(request,'inventory/add_show_produit.html',{'form':fm, 'prd':prod})    