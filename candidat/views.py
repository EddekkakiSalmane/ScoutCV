from django.shortcuts import render
from .models import *
from candidat.forms import *

# Create your views here.

# def candidat_create(request):
#     form = CandidatForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=CandidatForm()

#     context = {
#         'form' : form
#     }
#     return render(request , "candidats/createformCandidat.html",context)

def candidat_create(request):
    formExperience_Pro = Experience_ProForm(request.POST,prefix='formExperience_Pro')
    print(request.user)
    if formExperience_Pro.is_valid():        
        candidat = Candidat.objects.get(request.user)
        exp_pro = Experience_Pro.objects.get()
        candidat.Experience_Pro = exp_pro
        formExperience_Pro.create()

    context = {
        'formExperience_Pro' : formExperience_Pro
    }
    return render(request , "candidats/createformCandidat.html",context)