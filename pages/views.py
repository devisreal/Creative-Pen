from django.shortcuts import render
from .models import ContactDetail
from django.contrib import messages


def home(request):
   context = {}
   return render(request, 'pages/home.html', context)

def latest(request):
   context = {}
   return render(request, 'pages/latest_posts.html', context)

def categories(request):
   context = {}
   return render(request, 'pages/categories.html', context)

def about(request):
   context = {}
   return render(request, 'pages/about.html', context)

def contact(request):
   if request.method == 'POST':
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      email_address = request.POST['email']      
      message = request.POST['message']

      ContactDetail.objects.create(
         firstname=firstname,
         lastname=lastname, 
         email_address=email_address, 
         message=message
      )
      messages.success(request, 'Your message has been sent!')
   context = {}
   return render(request, 'pages/contact.html', context)