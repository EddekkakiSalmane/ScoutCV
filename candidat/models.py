from django.db import models

# Create your models here.
class Candidat(models.Model):
    SEX = (
        ('H','Homme'),
        ('F','Femme'),
    )
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    date_n = models.DateField()
    sex = models.CharField(max_length=1,choices=SEX,blank=False,default="")
    status = models.CharField(max_length=10)
    nationalite = models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    ville = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField(null=True,blank=True)
    email = models.EmailField(max_length=255)
    linkdin = models.URLField(max_length=200,null=True,blank=True)


    

