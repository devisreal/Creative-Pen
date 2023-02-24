from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from hitcount.models import Hit
from account.models import User, UserSettings
from blog.models import Post
import datetime
import pandas
from .forms import UserSocialHandleForm, UserUpdateForm

@login_required
def dashboard(request, slug):
   if slug != request.user.slug:      
      return redirect('users:dashboard', slug=request.user.slug)
   
   try:
      user = User.objects.get(slug=slug)
      liked_posts = Post.objects.filter(likes=user)
      author_posts = Post.objects.filter(post_author=user)
      total_hits = Hit.objects.all().count()
      total_users = User.objects.all()
      total_posts = Post.objects.all()
      total_posts_likes = 0      
      for post in Post.objects.all():
         total_posts_likes += post.likes.all().count()         
      total_likes = total_posts_likes
      
      user_values = total_users.values().order_by("date_joined")
      df = pandas.DataFrame(user_values)
      date_joined = df['date_joined'].tolist()
      sum_user_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      sum_user_list_prev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      for date in date_joined:
         if datetime.date.today().year == date.year:
            sum_user_list[date.month - 1] += 1
         elif datetime.date.today().year-1 == date.year:
            sum_user_list_prev[date.month - 1] += 1
      else:
         pass

   except User.DoesNotExist:
      return redirect('error_page')
      
   context = {
      'user': user,
      'liked_posts': liked_posts,
      'author_posts': author_posts,
      'total_users': total_users
   }

   if user.is_staff or user.is_superuser:
      context.update({
         'total_users': total_users.count(),
         'total_posts': total_posts.count(),
         'total_likes': total_likes,
         'total_hits': total_hits,
         'y1': sum_user_list,
         'y2': sum_user_list_prev,
      })
      return render(request, 'pen_admin/dashboard.html', context)
   else:      
      return render(request, 'users/dashboard.html', context)

@login_required
def share_liked_posts(request, slug):
   if slug != request.user.slug:        
      return redirect('users:edit_profile', slug=request.user.slug)
   
   user = User.objects.get(slug=slug)
   user_settings = UserSettings.objects.get(user=user)
   
   if user_settings.share_liked_posts == True:
      user_settings.share_liked_posts = False
      messages.success(
          request, "Operation successful! Other users will no longer see your liked posts")
   else:
      user_settings.share_liked_posts = True      
      messages.success(request, "Operation successful! Other users can now see your liked posts")

   user_settings.save()
   return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def request_author_access(request, slug, username):   
   reader_settings = UserSettings.objects.get(user__username=username)
   user = User.objects.get(username=username)
   if user.is_author:
      messages.warning(request, f'You are already an author!')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/')) 
   else:         
      reader_settings.request_author_access = True
      reader_settings.requested_date = datetime.datetime.now()
      reader_settings.save()      
      messages.success(request, f"Author access requested!")
      return redirect('users:dashboard', slug=slug)

@login_required()
def follow_user(request, slug, username):
   try:
      user_settings = UserSettings.objects.get(user__username=username)
      if user_settings.followers.filter(id=request.user.id).exists():
         user_settings.followers.remove(request.user)
         messages.success(request, f"You are no longer following '{user_settings.user.username}' ")
      else:
         user_settings.followers.add(request.user)
         messages.success(request, f"You are now following '{user_settings.user.username}' ")
      return HttpResponseRedirect(request.META['HTTP_REFERER'])
   except User.DoesNotExist:
      return redirect('error_page')

@login_required
def bookmarks(request, slug):
   if slug != request.user.slug:      
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
      liked_posts = Post.objects.filter(likes=user)
      if request.user == user:
         return redirect('users:profile', slug=slug)        
      elif user.is_author:
         if request.user.is_staff:
            return redirect('users:single_author', slug=request.user.slug, username=user.username)
         else:
            author_posts = Post.objects.filter(post_author=user)
            context = {
               'author': user,
               'user': user,
               'author_posts': author_posts,
               'liked_posts': liked_posts
            }
            return render(request, 'users/user-external.html', context)         
      else:
         context = {
            'reader': user,
            'user': user,
            'liked_posts': liked_posts
         }
         return render(request, 'users/user-external.html', context)
   except User.DoesNotExist:
      return redirect('error_page')
   
@login_required
def change_password(request, slug):
   if request.method == 'POST':
      form = PasswordChangeForm(request.user, request.POST)
      if form.is_valid():
         user = form.save()
         update_session_auth_hash(request, user)
         messages.success(request, 'Your password was successfully updated!')
         return redirect('users:profile', slug=slug)
      else:
         messages.error(request, 'Please correct the error below.')
   else:
      form = PasswordChangeForm(request.user)

   context = {
       'form': form
   }
   return render(request, 'users/change_password.html', context)
