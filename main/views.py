from django.shortcuts import render


def home(request):
    context={
        'judul':'kuliah pak huda',
        'kontributor':'Iftah Nur Fadlilah',
    }
    if request.method=='POST':
        print('ini method post')
    else:
        print('ini method get')
    return render(request, 'base.html',context)