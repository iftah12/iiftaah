from django.shortcuts import render
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
    return render(request, 'create.html',context)