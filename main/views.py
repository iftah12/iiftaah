from django.shortcuts import render
<<<<<<< HEAD
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
=======
from .form import ContactForms

def home(request):
    contact_form = ContactForms()
    context={
        'judul':'kuliah pak huda',
        'contact_form': contact_form
    }
    if request.method=='POST':
        print('ini method post')
        context['nama']=request.POST['nama']
        context['nim'] = request.POST['nim']
    else:
        print('ini method get')
    return render(request, 'base.html',context)
>>>>>>> 5963055aed21bda61510648b8bf23ea77affa2f5
