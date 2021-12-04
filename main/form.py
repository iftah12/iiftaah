from django import forms
from django.forms.fields import CharField

class ContactForms(forms.Form):
    nama=forms.CharField(max_length=20)
    nim=forms.CharField(max_length=20)