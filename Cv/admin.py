from django.contrib import admin
from .models import Cv,Experience_Pro,Language,Certificat,Projet_realise,Ecole,Academic



# Register your models here.
admin.site.register(Cv)
admin.site.register(Experience_Pro)

class Experience_ProInline(admin.TabularInline):
    model = Experience_Pro


class LanguageInline(admin.TabularInline):
    model = Language

class CertificatInline(admin.TabularInline):
    model = Certificat


class Projet_realiseInline(admin.TabularInline):
    model = Projet_realise

class EcoleInline(admin.TabularInline):
    model = Ecole

class AcademicInline(admin.TabularInline):
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

