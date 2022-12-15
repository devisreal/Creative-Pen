from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pages.models import ContactDetail, Subscriber
from account.models import User

# ! Staffs
@login_required
def staffs(request, slug):
   if not request.user.is_superuser:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      staffs = User.objects.filter(is_staff=True)
      context = {
         'staffs': staffs
      }
      return render(request, 'pen_admin/staffs.html', context)

@login_required
def staff_single(request, slug, username):
   if not request.user.is_superuser:
      messages.warning(request, 'You are not authorized to access that page')      
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:
      staff = User.objects.filter(is_staff=True).get(username=username)
      context = {
         'staff': staff
      }
      return render(request, 'pen_admin/single_staff.html', context)

# ! Authors
@login_required
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

@login_required
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


# ! Readers
@login_required
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
      
@login_required
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



# ! Subscribers
@login_required
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


@login_required
def delete_subscriber(request, slug, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      subscriber = Subscriber.objects.get(id=id)
      subscriber.delete()
      messages.success(request, 'Subscriber deleted!')
      return redirect('users:subscribers')      