from django.shortcuts import render
from .models import Candidat
from candidat.forms import CandidatForm

# Create your views here.

# def candidat_create(request):
#     my_form = CandidatForm()
#     if request.method == "POST":
#         my_form= CandidatForm(request.POST)
#         if my_form.is_valid():        
#             Candidat.objects.create(**my_form.cleaned_data)
#     context = {
#         "form": my_form
#     }
#     return render(request , "candidat/createformCandidat.html",context)

def candidat_create(request):
    form = CandidatForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=CandidatForm()

    context = {
        'form' : form
    }
    return render(request , "candidats/createformCandidat.html",context)
