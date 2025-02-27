from django.db import models


# Create your models here.
#Creation table User-client
class User(models.Model):
    name = models.CharField(max_length= 70)
    email = models.CharField(max_length=100)
    password =models.CharField(max_length=100)

#Creation table Produit
class Produit(models.Model):
    name_prod = models.CharField(max_length= 70)
    description = models.CharField(max_length=100)
    quantite =models.IntegerField()
    prix_unit =models.FloatField()

#Creation table Commande
class Commande(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    produit_id = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_cmd = models.IntegerField()
    commande_date = models.DateField()
 


