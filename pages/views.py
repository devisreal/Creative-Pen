from django.shortcuts import render, redirect
from .models import ContactDetail, Subscriber
from django.contrib import messages
from account.models import User


def home(request):
   authors = User.objects.filter(is_author=True)
   num_visits = request.session.get('num_visits', 0)
   request.session['num_visits'] = num_visits + 1
   context = {
      'authors': authors,
      'num_visits': num_visits
   }
   return render(request, 'pages/home.html', context)

def footer(request):
   if request.method == 'POST':      
      email = request.POST['email']      
      Subscriber.objects.create(email=email)
      
      messages.success(request, 'Thank you for subscribing! 👍')
      return redirect(request.META.get('HTTP_REFERER'))

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
      name = request.POST['name']
      subject = request.POST['subject']
      email_address = request.POST['email']      
      message = request.POST['message']

      ContactDetail.objects.create(
         name=name,
         subject=subject,
         email_address=email_address,
         message=message
      )
      messages.success(request, 'Your message has been sent!')
   context = {}
   return render(request, 'pages/contact.html', context)