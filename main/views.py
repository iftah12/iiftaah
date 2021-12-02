from django.shortcuts import render
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