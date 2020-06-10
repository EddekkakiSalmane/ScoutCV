from django.shortcuts import render
from Cv.forms import *

# Create your views here.

def cv_create(request):
    formAcademic = AcademicForm(request.POST,prefix='formAcademic')
    formExperience_Pro = Experience_ProForm(request.POST,prefix='formExperience_Pro')
    formProjet_realise = Projet_realiseForm(request.POST,prefix='formProjet_realise')
    formCertificat = CertificatForm(request.POST,prefix='formCertificat')
    formLanguage = LanguageForm(request.POST,prefix='formLanguage')
    formCv = CvForm(request.POST,prefix='formCv')
    
    if request.method == 'POST':
        print(request.POST)
        if formAcademic.is_valid() and formExperience_Pro.is_valid() and formProjet_realise.is_valid() and formCertificat.is_valid() and formLanguage.is_valid():
            formCv.save()
            print("yeeeees")
        else:
            formAcademic = AcademicForm(prefix='formAcademic')
            formExperience_Pro = Experience_ProForm(prefix='formExperience_Pro')
            formProjet_realise = Projet_realiseForm(prefix='formProjet_realise')
            formCertificat = CertificatForm(prefix='formCertificat')
            formLanguage = LanguageForm(prefix='formLanguage')



    context = {
        'formAcademic' : formAcademic,
        'formExperience_Pro' : formExperience_Pro,
        'formProjet_realise' : formProjet_realise,
        'formCertificat' : formCertificat,
        'formLanguage' : formLanguage,
        'formCv' : formCv
    }
    return render(request , "Cvs/createCV.html",context)