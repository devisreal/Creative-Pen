from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserSocialHandleForm, UserUpdateForm
from django.contrib import messages
from account.models import User, UserSettings
from account.views import user_logout
from datetime import datetime
from blog.models import Post


@login_required
def dashboard(request, slug):
   if slug != request.user.slug:      
      return redirect('users:dashboard', slug=request.user.slug)
   try:
      user = User.objects.get(slug=slug)
      liked_posts = Post.objects.filter(likes=user)
      author_posts = Post.objects.filter(post_author=user)
   except User.DoesNotExist:
      return redirect('error_page')
   else:
      context = {
         'user': user,
         'liked_posts': liked_posts,
         'author_posts': author_posts
      }
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
def bookmarks(request, slug):
   if slug != request.user.slug:
      messages.error(request, "You're not allowed to access this account")
      return redirect('users:bookmarks', slug=request.user.slug)
   try:
      user = User.objects.get(slug=slug)
      bookmarks = Post.objects.filter(bookmarks=request.user)
   except User.DoesNotExist:
      return redirect('error_page')
   else:
      context = {
         'user': user,
         'bookmarks': bookmarks
      }
      return render(request, 'users/bookmarks.html', context)   

@ login_required
def bookmark_add(request, slug, id):
   post = get_object_or_404(Post, id=id)
   if post.bookmarks.filter(id=request.user.id).exists():
      post.bookmarks.remove(request.user)
      messages.success(request, "Post removed from bookmarks")
   else:   
      post.bookmarks.add(request.user)
      messages.success(request, "Post added to bookmarks")
   return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def like_post(request, slug, id):
   post = get_object_or_404(Post, id=id)
   if post.likes.filter(id=request.user.id).exists():
      post.likes.remove(request.user)   
   else:
      post.likes.add(request.user)      
   return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def user_profile(request, slug):   
   if slug != request.user.slug:  
      messages.error(request, "You're not allowed to access this account")    
      return redirect('users:profile', slug=request.user.slug)
   try:
      user = User.objects.get(slug=slug)
   except User.DoesNotExist:
      return redirect('error_page')
   context = {
      "user": user
   }
   return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request, slug):
   if slug != request.user.slug:  
      messages.error(request, "You're not allowed to access this account")    
      return redirect('users:edit_profile', slug=request.user.slug)

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


def user_external(request, slug):
   try:
      user = User.objects.get(slug=slug)
      if request.user == user:
         return redirect('users:profile', slug=slug)        
      elif user.is_author:
         if request.user.is_staff:
            return redirect('users:single_author', slug=request.user.slug, username=user.username)
         else:
            author_posts = Post.objects.filter(post_author=user)
            context = {
               'author': user,
               'author_posts': author_posts
            }
            return render(request, 'users/user-external.html', context)
         
      else:
         context = {
            'reader': user
         }
         return render(request, 'users/user-external.html', context)
   except User.DoesNotExist:
      return redirect('error_page')
         
