from django.db import models
from candidat.models import Candidat

# Create your models here.
class Experience_Pro(models.Model):
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()
    description_exp_pro = models.TextField(null=True,blank=True)

class Language(models.Model):
    langue = models.CharField(max_length=20)
    level = models.TextField(null=True,blank=True)
    
class Certificat(models.Model):
    accreditation = models.CharField(max_length=100)
    titre_cert = models.CharField(max_length=50)
    date_cert = models.IntegerField()

class Projet_realise(models.Model):
    annee_prjet = models.IntegerField()
    description_projet = models.TextField(null=True,blank=True)

class Ecole(models.Model):
    nom_ecole = models.CharField(max_length=50)
    classement = models.IntegerField()

class Academic(models.Model):
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()
    type_diplome = models.CharField(max_length=10)
    description_academic = models.TextField(null=True,blank=True)
    ecole = models.ForeignKey('Ecole' , on_delete=models.DO_NOTHING)

class Cv(models.Model):
    experience_Pro = models.ForeignKey('Experience_Pro' ,on_delete=models.CASCADE)
    language = models.ForeignKey('Language',on_delete=models.CASCADE)
    certificat = models.ForeignKey('Certificat',on_delete=models.CASCADE)
    projet_realise = models.ForeignKey('Projet_realise',on_delete=models.CASCADE)
    academic = models.ForeignKey('Academic',on_delete=models.CASCADE)
    candidat = models.ForeignKey('candidat.Candidat',on_delete=models.CASCADE ,unique=True)


