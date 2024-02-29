from django.forms import ModelForm
from valve import models
import datetime
from django import forms




class contform(ModelForm):
    class Meta:
        model=models.Contact
        fields=['nom', 'email', 'subject', 'message']
        widgets= {
            "nom": forms.TextInput(attrs={'class':'form-control text-black'}),
            "email":forms.EmailInput(attrs={'class':'form-control text-black','type':'email'}), 
            "subject": forms.TextInput(attrs={'class':'form-control text-black'}),
            "message":forms.Textarea(attrs={'class':'form-control text-black'}),
        
        }







 