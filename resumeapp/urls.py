from django.contrib import admin
from django.urls import path, include
from resumeapp import views

urlpatterns = [
   path('', views.home, name='home'),
   path('contact/', views.contact, name='contact'),
   path('intro/', views.intro, name='intro'),
   path('myproject/', views.myproject, name='myproject'),
]
