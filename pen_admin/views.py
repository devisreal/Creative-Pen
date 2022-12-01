from django.shortcuts import render, redirect
from django.contrib import messages
from pages.models import ContactDetail, Subscriber
from account.models import User

def authors(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      authors = User.objects.filter(is_author=True)
      context = {
         'authors': authors
      }
      return render(request, 'pen_admin/authors.html', context)

def readers(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      readers = User.objects.filter(is_author=False)
      context = {
         'readers': readers
      }
      return render(request, 'pen_admin/readers.html', context)
      
def subscribers(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      subscribers = Subscriber.objects.all()
      context = {
         'subscribers': subscribers
      }
      return render(request, 'pen_admin/subscribers.html', context)