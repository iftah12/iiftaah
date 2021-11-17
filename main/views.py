from django.shortcuts import render


def home(request):
    context={
        'judul':'kuliah pak huda',
        'kontributor':'Iftah Nur Fadlilah',
    }
    return render(request, 'base.html',context)
