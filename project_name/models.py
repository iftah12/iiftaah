from django.db import models

class ContactModel(models.Model):
    nama=models.CharField(max_length=20)
    nim=models.CharField(max_length=20)
    