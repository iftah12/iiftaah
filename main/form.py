from django import forms
from django.forms.fields import CharField

class ContactForms(forms.Form):
    nama=forms.CharField()
    nim=forms.CharField()
    