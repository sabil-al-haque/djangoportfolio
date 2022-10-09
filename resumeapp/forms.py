from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['name', 'email','subject','message']
    labels = {'name':'Enter Your Name', 'email':'Enter Your Email','subject':'Enter Your Subject','message':'Enter Your Message'}
    widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'}),'subject':forms.TextInput(attrs={'class':'form-control'}),'message':forms.TextInput(attrs={'class':'form-control'  }),} 