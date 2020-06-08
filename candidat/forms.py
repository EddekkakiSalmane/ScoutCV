from django import forms
from candidat.models import Candidat

class CandidatForm(forms.ModelForm):
    # SEX = (
    #     ('H','Homme'),
    #     ('F','Femme'),
    # )
    nom         =forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nom"}))
    prenom      =forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Prenom"}))
    date_n         =forms.DateField(label = 'Date de naissance')
    # #sex         = forms.CharField(max_length=1,choices=SEX,blank=False,default="")
    status      = forms.CharField(max_length=10,widget=forms.TextInput(attrs={"placeholder": "célibataire ,marié(e) ,veuf(ve) ,divorcé(e)"}))
    # nationalite = forms.CharField(max_length=20)
    # pays        = forms.CharField(max_length=20)
    # ville       = forms.CharField(max_length=20)
    # telephone   = forms.CharField(max_length=20)
    adresse    = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "rows":4,
                                "cols":20,                                
                            }
                        )
                        )
    email       = forms.EmailField(max_length=255)
    # linkdin     = forms.CharField(max_length=20)

    class Meta: 
        model = Candidat     
        fields = "sex","nationalite","pays","ville","telephone","linkdin"
