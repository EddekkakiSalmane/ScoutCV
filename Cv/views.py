from django.shortcuts import render
from Cv.forms import CvForm

# Create your views here.

def cv_create(request):
    form = CvForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=CvForm()

    context = {
        'form' : form
    }
    return render(request , "Cvs/createCV.html",context)