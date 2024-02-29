from django.forms import ModelForm
from valve import models
import datetime
from django import forms



class actual_form(ModelForm):
    class Meta:
        model=models.Actualite
        fields=['titre', 'contenu', 'date_publication', 'auteur', 'categorie', 'image','Document']
        widgets= {
            "Document":forms.Select(choices=models.DOCUMENT,attrs={'class':'form-control'}),
            "titre":forms.TextInput(attrs={'class':'form-control text-black'}),
            "contenu":forms.Textarea(attrs={'class':'form-control text-black'}),
            "date_publication":forms.DateInput(attrs={'class':'form-control text-black'}),
            "auteur":forms.Select(choices=models.AUTEURS,attrs={'class':'form-control'}),
            "categorie":forms.Select(choices=models.CATEGORIE_ACTU,attrs={'class':'form-control'}),
            "image":forms.FileInput(attrs={'class':'form-control text-black'})


        }







