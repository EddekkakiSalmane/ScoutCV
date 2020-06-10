from django import forms
from candidat.models import *

class CandidatForm(forms.ModelForm):
    class Meta: 
        model = Candidat     
        fields = ["nom",
        "prenom",
        "date_n",
        "sex",
        "status",
        "nationalite",
        "pays",
        "ville",
        "telephone",
        "adresse",
        "email",
        "linkdin"]


class AcademicForm(forms.ModelForm):
    class Meta: 
        model = Projet_realise
        fields = ("__all__")

class Experience_ProForm(forms.ModelForm):
    class Meta: 
        model = Experience_Pro
        fields = ["__all__"]


class Projet_realiseForm(forms.ModelForm):
    class Meta: 
        model = Projet_realise
        fields = ("__all__")


class CertificatForm(forms.ModelForm):
    class Meta: 
        model = Certificat
        fields = ("__all__")


class LanguageForm(forms.ModelForm):
    class Meta: 
        model = Language
        fields = ("__all__")

