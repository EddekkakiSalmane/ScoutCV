from django import forms
from Cv.models import Cv,Experience_Pro,Projet_realise,Ecole,Academic,Language,Certificat

class CvForm(forms.Form):
    annee_debut = forms.IntegerField()
    annee_fin = forms.IntegerField()
    description_exp_pro = forms.CharField(max_length=100)

    annee_prjet = forms.IntegerField()
    description_projet = forms.CharField(max_length=100)

    class Meta: 
        model = Cv     
        fields = "Ecole"

    annee_debut = forms.IntegerField()
    annee_fin = forms.IntegerField()
    type_diplome = forms.CharField(max_length=10)
    description_academic = forms.CharField(max_length=100)
    
    langue = forms.CharField(max_length=20)
    level = forms.IntegerField()

    accreditation = forms.CharField(max_length=100)
    titre_cert = forms.CharField(max_length=50)
    date_cert = forms.IntegerField()

   