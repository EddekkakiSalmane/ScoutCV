from django.contrib import admin
from .models import Cv,Experience_Pro,Language,Certificat,Projet_realise,Ecole,Academic



# Register your models here.
admin.site.register(Cv)

class Experience_ProInline(admin.StackedInline):
    model = Experience_Pro


class LanguageInline(admin.StackedInline):
    model = Language

class CertificatInline(admin.StackedInline):
    model = Certificat


class Projet_realiseInline(admin.StackedInline):
    model = Projet_realise

class EcoleInline(admin.StackedInline):
    model = Ecole

class AcademicInline(admin.StackedInline):
    model = Academic

class CvModelsAdmin(admin.ModelAdmin):
    inlines = [ 
        Experience_ProInline,
        LanguageInline,
        CertificatInline,
        Projet_realiseInline,
        EcoleInline,
        AcademicInline
    ]

