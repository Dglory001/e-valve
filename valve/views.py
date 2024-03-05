from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User 
from django.views.generic import View
from django.http import HttpResponseRedirect
from valve.forms.actu_form import actual_form
from valve.forms.doc_form import FormulaireDocument
from valve.forms.zonsuggest_form import contform
from django import forms
from django.contrib.auth import authenticate, login
from django.conf.urls.static import static
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import render
from .models import Actualite





# Create your views here.
def home(request):
    try:
        image1 = ConfigImage.objects.get(pk=4) 
        image2 = ConfigImageAccueil.objects.get(pk=3)
        image3 = ConfigImageAccueil.objects.get(pk=3)
        textehome1 = TextAccueil.objects.all()
   
        
        

        
        context={
            "titre":"home",
            "image1":image1,
            "image2":image2,
            "image3":image3,
            "textehome1":textehome1,
           
        }     
        # Create a response
        response = TemplateResponse(request,'index.html', context)  
        
        # Return the response
        return response
    
    
        
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR - Formulaire invalide")
     
# Creation views actualites
         
        
# Create views Documents
def doc(request):
    try:
 
        document = Document.objects.all()
        context={
            "titre":"doc",
            "document":document
        }     
    
        # Create a response
        response = TemplateResponse(request,'document.html', context)  
        
        # Return the response
        return response
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR - Formulaire invalide")




# Create views Annonces Inspecteurs
def ann_igf(request):
  
    try:

        image = ConfigImageigf.objects.get(pk=4)
        textbloc = TextAnnonceigf.objects.all()
        textinfodedie = data_toggleigf.objects.all()
        context={
            "titre":"ann_igf",
            "image":image,
            "textbloc":textbloc,
            "textinfodedie":textinfodedie
           
        }     
        # Create a response
        response = TemplateResponse(request,'annonceigf.html', context)  
        
        # Return the response
        return response
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR - Formulaire invalide")
    
    
# Create views Annonces Saft
def ann_saft(request):
    try:
        image = ConfigImageigf.objects.get(pk=5)
        textblocsaft = TextAnnoncesaft.objects.all()
        textdatatoggle = data_toggleSaft.objects.all()
        context={
            "titre":"ann_saft",
             "image":image,
             "textblocsaft":textblocsaft,
             "textdatatoggle":textdatatoggle
        }     
        # Create a response
        response = TemplateResponse(request,'annoncesaft.html', context)  
        
        # Return the response
        return response
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR - Formulaire invalide")
    
    
# Create views Blog
def blog_interne(request):
    try:
      
        imageBlogint1 =Configimageblog1.objects.get(pk=1)
        imageBlogint_all =Configimageblog1.objects.all()
        titreblog1= Configimageblog1.objects.all()
        parablog1= Configimageblog1.objects.all()
        datblog1=Configimageblog1.objects.all()
           
        context={
            "titre":"blog_interne",
            "imageBloginterne":imageBlogint1,
            "titreblog1":titreblog1,
            "paragrapheblog1":parablog1,
            "datblog1":datblog1,
            "imageBlogint_all":imageBlogint_all
         
         
        }     
        # Create a response
        response = TemplateResponse(request,'blog.html', context) 
        #return render(request, 'valve/blog.html', {'textvoirplus': textvoirplus}) 
        
        # Return the response
        return response
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR - Formulaire invalide")

# Create views Blog
def projet(request):
    try:
        txtprojetitre1_all= TextProjetParagraph1.objects.all()
        txtparaprojet1= TextProjetParagraph1.objects.all()
        imgprojet_all= TextProjetParagraph1.objects.all()
        txtimageprojet_all=TextProjetParagraph1.objects.all()

       
       
        context={
            "titre":"service",
            "txtprojetitre1":txtprojetitre1_all,
            "txtparaprojet1":txtparaprojet1,
            "imgprojet_all":imgprojet_all,
            "txtimageprojet_all":txtimageprojet_all
           
           
        }     
        # Create a response
        response = TemplateResponse(request,'projets.html', context)  
        
        # Return the response
        return response
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR - Formulaire invalide")
    


# Create views Annonce Accueil
def actu_accueil(request):
    try:
      
        context={
            "titre":"actu_accueil",
        }     
        # Create a response
        response = TemplateResponse(request,'actuaccueil.html', context)  
        
        # Return the response
        return response
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR - Formulaire invalide")


# Create your views FormsEnregistrement here.
def form_actual(request):
    try:
        form=actual_form()
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = actual_form(request.POST, request.FILES)
            # check whether it's valid:
            if form.is_valid():
                p=Actualite()
                p.Document = form.cleaned_data["Document"]
                p.titre = form.cleaned_data["titre"]
                p.contenu = form.cleaned_data["contenu"]
                p.date_publication = form.cleaned_data["date_publication"]
                p.auteur = form.cleaned_data["auteur"]
                p.categorie = form.cleaned_data["categorie"]
                p.image = form.cleaned_data["image"]
                p.save()
               
                return redirect("form_actual")
  
                # if a GET (or any other method) we'll create a blank form
            else:
                form = actual_form()
        context={
            "titre":"forms",
            "transparent":True,
            "form":form
        }     
        # Create a response
         
        # Return the response
        return render(request, 'formactu.html', context)
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR -",e)
    

# Create your views FormsEnregistrement here.
def formajout_doc(request):
    try:
    
        form = FormulaireDocument()
        if request.method == "POST":
            form = FormulaireDocument(request.POST, request.FILES)
            if form.is_valid():
                p = Document()
                p.nomdocument = form.cleaned_data["nomdocument"]
                p.fichier = form.cleaned_data["fichier"]
                p.type_doc = form.cleaned_data["type_doc"]
                p.save()

                # Redirection possible à modifier (vers une page de confirmation, par exemple)
                return redirect("formajout_doc")
        else:
            # Réinitialiser le formulaire uniquement si ce n'est pas une soumission POST
            form = FormulaireDocument()

        context = {
            "titre": "Formulaires",  # Capitalisé
            "transparent": True,
            "form": form,
        }
        return render(request, 'formdocajout.html', context)
    except (ValueError, TypeError) as e:
        # Log the error for debugging
        print('###### ', e)
        return HttpResponse("Une erreur s'est produite.")  # Generic error message
    else:
        # Code exécuté si aucune exception n'est rencontrée
        pass

# Formulaire Suggestion
def contactform(request):
    print('je suis forte')
    try:
        form = contform()
        if request.method == "POST":
            form = contform(request.POST, request.FILES)
            if form.is_valid():
                p = Suggestion()
                p.nom = form.cleaned_data["nom"]
                p.email = form.cleaned_data["email"]
                p.subject = form.cleaned_data["subject"]
                p.message = form.cleaned_data["message"]
                p.save()

                # Redirection possible à modifier (vers une page de confirmation, par exemple)
                return redirect("contactform")
        else:
            # Réinitialiser le formulaire uniquement si ce n'est pas une soumission POST
            form = contform()

        context={
            "titre":"forms",
            "transparent":True,
            "form":form
         }
        return render(request, 'zonesuggestion.html', context)
    except (ValueError, TypeError) as e:
        # Log the error for debugging
        print('###### ', e)
        return HttpResponse("Une erreur s'est produite.")  # Generic error message
    else:
        # Code exécuté si aucune exception n'est rencontrée
        pass


# Liste des Actualités Publiés
def listactualitepub(request):
    
    try:
        
        model=Actualite.objects.all()
       


        context={
            "titre":"listactualitepub",
            "transparent":True,
            "model":model
        }     
        # Create a response
        response = TemplateResponse(request,'listactualites.html', context)  

        # Return the response
        return response
    
    
    except Exception as e:
         print('###### ',e)
         return HttpResponse("ERROR -",e)
         
         return render(request, 'template.html', {'objets': objets_page})

