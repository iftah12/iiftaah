from django.urls import path

from . import views
app_name = 'main'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.home, name='home'),
]