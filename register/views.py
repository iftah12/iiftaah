from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def base(request):
    return render(request, 'register.html')
def about(request):
    return HttpResponse('<marquee>Ini adalah halaman about</marquee>')
