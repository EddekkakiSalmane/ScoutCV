from django import forms
from candidat.models import Candidat

class CandidatForm(forms.ModelForm):
    class Meta: 
        model = Candidat     
        fields = "__all__"
