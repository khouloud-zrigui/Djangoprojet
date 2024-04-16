from django.shortcuts import render, HttpResponseRedirect
from .forms import ClientRegistration
from .models import User
from .models import Produit
from .models import Commande
from .forms import ProduitRegistration
from .forms import CommandeRegistration

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
        return render(request,'inventory/add_show_client.html')
    
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

#Cette fonction permet de modifier les informations produit
def update_produit(request,id):
    if request.method =='POST':
        pr = Produit.objects.get(pk = id)
        fm = ProduitRegistration(request.POST, instance= pr)
        if fm.is_valid():
            fm.save()
    else:
        pr = Produit.objects.get(pk =id)
        fm = ProduitRegistration(instance=pr)
                
    return render(request, 'inventory/update_produit.html',{'form':fm})

#cette fonction permet de supprimer les données produit par id
def delete_produit(request,id):
    if request.method == 'POST':
        pr = Produit.objects.get(pk = id)
        pr.delete()
        return HttpResponseRedirect('/')

#cette fonction permet d'ajouter une commande  
def add_get_commande(request):
    if request.method == 'POST':
        fm = CommandeRegistration(request.POST)
        if fm.is_valid():
            cl_id = fm.cleaned_data['client_id']
            pr_id = fm.cleaned_data['produit_id']
            qy_cmd = fm.cleaned_data['quantite_cmd']
            dt_cm = fm.cleaned_data['commande_date']
           
            reg = Commande(client_id=cl_id, produit_id=pr_id, quantite_cmd=qy_cmd, commande_date=dt_cm)
            reg.save()
            fm = CommandeRegistration()
            
    else:
        fm = CommandeRegistration()   
    cmd = Commande.objects.all()
    return render(request, 'inventory/add_show_commande.html', {'form': fm, 'comd': cmd})



#Cette fonction permet de modifier les informations d'une commande
def update_commande(request,id):
    if request.method =='POST':
        commd = Commande.objects.get(pk = id)
        fm = CommandeRegistration(request.POST, instance= commd)
        if fm.is_valid():
            fm.save()
    else:
        commd  = Commande.objects.get(pk =id)
        fm = CommandeRegistration(instance=commd )
                
    return render(request, 'inventory/update_commande.html',{'form':fm})

#cette fonction permet de supprimer les données d'une commande  par id
def delete_commande(request,id):
    if request.method == 'POST':
        commd = Commande.objects.get(pk = id)
        commd.delete()
        return HttpResponseRedirect('/')


def home(request):
    return render(request, 'inventory/home.html')

