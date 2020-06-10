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
    sex = models.CharField(max_length=1,choices=SEX,blank=False,default="H")
    status = models.CharField(max_length=10)
    nationalite = models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    ville = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField(null=True,blank=True)
    email = models.EmailField(max_length=255)
    linkdin = models.URLField(max_length=200,null=True,blank=True)
    academic = models.ForeignKey('Academic',on_delete=models.CASCADE,null=True)
    experience_Pro = models.ForeignKey('Experience_Pro' ,on_delete=models.CASCADE,null=True)
    projet_realise = models.ForeignKey('Projet_realise',on_delete=models.CASCADE,null=True)
    certificat = models.ForeignKey('Certificat',on_delete=models.CASCADE,null=True)
    language = models.ForeignKey('Language',on_delete=models.CASCADE,default='')

class Ecole(models.Model):
    nom_ecole = models.CharField(max_length=50)
    classement = models.IntegerField()

class Academic(models.Model):
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()
    type_diplome = models.CharField(max_length=10)
    description_academic = models.TextField(null=True,blank=True)
    ecole = models.ForeignKey('Ecole' , on_delete=models.DO_NOTHING)


class Experience_Pro(models.Model):
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()
    description_exp_pro = models.TextField(null=True,blank=True)


class Projet_realise(models.Model):
    annee_projet = models.IntegerField()
    description_projet = models.TextField(null=True,blank=True)

class Certificat(models.Model):
    accreditation = models.CharField(max_length=100)
    titre_cert = models.CharField(max_length=50)
    date_cert = models.IntegerField()


class Language(models.Model):
    lvl = (
        ('A1','découverte'),
        ('A2','usuel'),
        ('B1','niveau seuil'),
        ('B2','niveau avancé'),
        ('C1','autonome'),
        ('C2','maîtrise'),
    )
    langue = models.CharField(max_length=20)
    level = models.CharField(max_length=2,choices=lvl,blank=False,default="A1")
    


