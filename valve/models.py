from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib import admin
from django.db import models


TYPE_DOCUMENT=[
    ("Décision", "Décision"),
    ("Note","Note"),
    ("Communiqué Officiel", "Communiqué Officiel"),
    ("Autres","Autres"),
    ("lettre","Lettre"),
    ("Communiqué Interne","Communiqué Interne"),
]


ACTUALITES=[
    ("Actualité Culturelle","Actualité Culturelle"),
    ("Actualité Sociale","Actualité Sociale"),
    ("Actualité Sportive", "Actualité Sportive"),
    ("Actualité Scientifique et Technologique","Actualité Scientifique et Technologique"),
    ("Actualité Locale","Actualité Locale"),
    ("Autres", "Autres"),

]

AUTEURS=[
    ("Chef de Service","Chef de Service"),
    ("Chef de Service Adjoint","Chef de Service Adjoint"),
    ("Coordonateur","Coordonateur"),
    ("Coordonateur Adjoint","Coordonateur Adjoint"),
    ("Directeur","Directeur"),
    ("Chef de Division","Chef de Division"),
    ("Chef de Bureau","Chef de Bureau"),
    ("Assistant Directeur","Assistant Directeur"),
    ("Autres","Autres"),
]

DOCUMENT=[
    ("Actes administratifs","Actes administratifs"),
    ("Documents de travail","Documents de travail"), 
    ("Documents d'information","Documents d'information"),
    ("Documents patrimoniaux","Documents patrimoniaux"),
    ("Documents juridiques","Documents juridiques"),
    ("Documents scientifiques","Documents scientifiques"),
    ("Documents divers","Documents divers"),
    ("Autres","Autres"),
]

CATEGORIE_ACTU=[
     ("Annonce d'un évenement","Annonce d'un évenement"),
     ("Compte rendu d'un évenement à venir","Compte rendu d'un évenement à venir"),
     ("Compte rendu d'un évenement passé","Compte rendu d'un évenement passé"),
     ("Invitation à un évenement","Invitation à un évenement"),
     ("Avis de Sécurité","Avis de Sécurité"),
     ("Annonce d'un nouveau programme","Annonce d'un nouveau programme"),
     ("Annonce d'un évenement","Annonce d'un évenement"),
     ("Autres","Autres"),

]

# Documents
class Document(models.Model):
    nomdocument = models.CharField(max_length = 250, null = True, blank = True)
    fichier = models.FileField(blank=True,null=True,upload_to='document/%Y/%m/%d/')
    type_doc = type_doc = models.CharField(max_length=100,choices=TYPE_DOCUMENT,)

    def __str__(self):
        return (self.nomdocument)

# Actualités
class Actualite(models.Model):
    Document=models.ForeignKey("Document",related_name="actualite" ,blank=True, null=True, on_delete=models.CASCADE)
    titre = models.CharField(max_length = 250, null = True, blank = True)
    contenu = models.TextField( null = True, blank = True)
    date_publication  = models.DateField(blank=True, null=True)
    auteur = models.CharField(max_length=250,choices=AUTEURS,null = True, blank = True)
    categorie = models.CharField(max_length=255,choices=CATEGORIE_ACTU, null=True, blank =True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    def __str__(self):
        return str(self.titre)
    
#Contact
class Contact(models.Model):
    nom=models.CharField(max_length = 250, null = True, blank = True)
    email=models.EmailField(blank=True,null=True)
    subject=models.CharField(max_length = 250, null = True, blank = True)
    message=models.TextField( null = True, blank = True)
    def __str__(self):
        return str(self.nom)

    


# Images
class ConfigImage(models.Model):
     icon=models.ImageField(upload_to="images/")
     iconInsp=models.ImageField(upload_to="images/")
    
     def __str__(self):
        return str(self.icon)
     

class ConfigImageigf(models.Model):
     imagepageigf=models.ImageField(upload_to="images/")
     imagesaft=models.ImageField(blank=True,null=True,upload_to='configImage/%Y/%m/%d/')
     imageservice1=models.ImageField(blank=True,null=True,upload_to='configImage/%Y/%m/%d/')
     imageservice2=models.ImageField(blank=True,null=True,upload_to='configImage/%Y/%m/%d/')
     imageservice3=models.ImageField(blank=True,null=True,upload_to='configImage/%Y/%m/%d/')
     
     def __str__(self):
        return str(self.imagepageigf)
     
class ConfigImageAccueil(models.Model):
    imageaccueil1=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')
    imageaccueil2=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')
    imageaccueil3=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')
     
    def __str__(self):
        return str(self.imageaccueil1)
    
class Configimageblog(models.Model):
    imageblog1=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')
    imageblog2=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')
    imageblog3=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')
    imageblog4=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')
    imageblog5=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')
    imageblog6=models.ImageField(blank=True, null=True,upload_to='configImage/%Y/%m/%d/')

    def __str__(self):
        return str(self.imageblog1)
     
class  TextAccueil(models.Model):
    paraphe1=models.TextField(null = True, blank = True)
    
    def __str__(self):
        return str(self.paraphe1)
     
class TextAnnonceigf(models.Model):
    bloc1=models.TextField(null = True, blank = True)
    bloc2=models.TextField(null = True, blank = True)
    bloc3=models.TextField(null = True, blank = True)

    def __str__(self):
        return str(self.bloc1)

class data_toggleigf(models.Model):
    infoDedie_chefBrig=models.TextField(null= True, blank= True)
    infoDedie_igf=models.TextField(null = True, blank = True)
    infoDedie_if=models.TextField(null = True, blank = True)

    def __str__(self):
        return str(self.infoDedie_chefBrig)
    

class TextAnnoncesaft(models.Model):
    blocsaft1=models.TextField(null = True, blank = True)
    blocsaft2=models.TextField(null = True, blank = True)

    def __str__(self):
        return str(self.blocsaft1)

class data_toggleSaft(models.Model):
    infodediecadre=models.TextField(null = True, blank = True)
    infodediecolla=models.TextField(null = True, blank = True)
    infosenction=models.TextField(null = True, blank = True)

def __str__(self):
  return str(self.infodediecadre)