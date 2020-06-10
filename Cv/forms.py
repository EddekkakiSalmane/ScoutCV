from django import forms
from Cv.models import *

class AcademicForm(forms.ModelForm):
    class Meta: 
        model = Projet_realise
        fields = ("__all__")

class Experience_ProForm(forms.ModelForm):
    class Meta: 
        model = Experience_Pro
        fields = ("__all__")


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

class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = "__all__"