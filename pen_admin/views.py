from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from pages.models import ContactDetail, Subscriber
from account.models import User

def authors(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      authors = User.objects.filter(is_author=True)
      context = {
         'authors': authors
      }
      return render(request, 'pen_admin/authors.html', context)

def author_single(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')      
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:
      author = User.objects.filter(is_author=True).get(username=username)
      context = {
         'author': author
      }
      return render(request, 'pen_admin/single_author.html', context)

def readers(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      readers = User.objects.filter(is_author=False)
      context = {
         'readers': readers
      }
      return render(request, 'pen_admin/readers.html', context)
      
def reader_single(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:   
      reader = User.objects.filter(is_author=False).get(username=username)
      context = {
         'reader': reader
      }
      return render(request, 'pen_admin/single_reader.html', context)


def subscribers(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      subscribers = Subscriber.objects.all()
      context = {
         'subscribers': subscribers
      }
      return render(request, 'pen_admin/subscribers.html', context)