from django import forms
from django.forms.fields import CharField

class ContactForms(forms.Form):
<<<<<<< HEAD
    nama=forms.CharField(max_length=20)
    nim=forms.CharField(max_length=20)
=======
    nama=forms.CharField()
    nim=forms.CharField()
    
>>>>>>> 5963055aed21bda61510648b8bf23ea77affa2f5
