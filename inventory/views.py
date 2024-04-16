from django.shortcuts import render
from .forms import ClientRegistration
from .models import User

# Create your views here.
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
    else:
        fm = ClientRegistration()    
    return render(request,'inventory/add_show_client.html',{'form':fm})