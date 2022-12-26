from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserSocialHandleForm, UserUpdateForm
from django.contrib import messages
from account.models import User, UserSettings
from account.views import user_logout
from datetime import datetime



@login_required
def dashboard(request, slug):     
   
   context = {}
   return render(request, 'users/dashboard.html', context)

@login_required
def request_author_access(request, slug, username):   
   reader_settings = UserSettings.objects.get(user__username=username)
   user = User.objects.get(username=username)
   if user.is_author:
      messages.warning(request, f'You are already an author!')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/')) 
   else:         
      reader_settings.request_author_access = True
      reader_settings.requested_date = datetime.now()            
      reader_settings.save()      
      messages.success(request, f"Author access requested!")
      return redirect('users:dashboard', slug=slug)

@login_required
def user_profile(request, slug):   
   context = {

   }
   return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request, slug):
   if request.method == "POST":
      user_form = UserUpdateForm(request.POST or None, request.FILES or None, instance = request.user)
      social_form = UserSocialHandleForm(request.POST or None, request.FILES or None, instance = request.user.socialhandle ) 

      if user_form.is_valid() and social_form.is_valid():
         user_form.save()
         social_form.save()
         return redirect('users:profile', slug=slug)
      else:
         messages.error(request, "Enter all correct details.")
         return redirect(request.META.get("HTTP_REFERER"))
   else:
      user_form = UserUpdateForm(instance=request.user)
      social_form = UserSocialHandleForm(instance=request.user.socialhandle)   

   context = {
      'user_form': user_form,
      'social_form': social_form
   }   
   return render(request, 'users/edit_profile.html', context)

@login_required
def delete_account(request, slug):
   user = User.objects.get(slug=slug)
   user.is_active = False
   user.save()
   messages.success(request, "Account deleted successfully! 👋")
   return redirect('logout')


def author_external(request, slug):   
   author = User.objects.get(slug=slug)
   if request.user == author:
      return redirect('users:profile', slug=slug)   
   else:
      context = {
         'author': author
      }
      return render(request, 'users/author-external.html', context)
   