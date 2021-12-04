from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import ContactForms
from .models import ContactModel

def home(request):
    data = ContactModel.objects.all()
    context={
        'judul':'kuliah pak huda',
        'data': data
    }
    return render(request, 'base.html',context)
def create(request):
    contact_form = ContactForms()
    
    if request.method=='POST':
        ContactModel.objects.create(
            nama=request.POST['nama'],
            nim= request.POST['nim']
        )
        return HttpResponseRedirect("/")


    else:
        print('ini method get')
    context={
        'judul':'kuliah pak huda',
        'contact_form': contact_form
    }
    
    return render(request, 'create.html',context)