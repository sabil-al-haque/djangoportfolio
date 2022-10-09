from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'resumeapp/home.html') 

def intro(request):
    return render(request, 'resumeapp/intro.html') 

def myproject(request):
    return render(request, 'resumeapp/myproject.html') 
    
# def contact(request):
#     return render(request, 'resumeapp/contact.html') 


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string('resumeapp/emails/contactform.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            })

            send_mail('The contact form subject', 'This is the message', 'customer@gmail.com', ['sabilbup2018@gmail.com'], html_message=html)
            # https://mailtrap.io/inboxes ei link e giye mail ta dekha jabe
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'resumeapp/contact.html', {
        'form': form
    })
