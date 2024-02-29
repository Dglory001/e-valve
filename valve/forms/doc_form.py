from django.db import models
from valve import models  
from django.forms import ModelForm
from django import forms

class FormulaireDocument(ModelForm):
    class Meta:
        model = models.Document
        fields = ['nomdocument', 'fichier', 'type_doc']

        widgets = {
            "nomdocument": forms.TextInput(attrs={'class':'form-control text-black'}),
            "fichier": forms.FileInput(attrs={'class':'form-control text-black','type':'file','name':'fichier'}),
            "type_doc": forms.Select(choices=models.TYPE_DOCUMENT,attrs={'class':'form-control',"placeholder":"Ville"}),
        }