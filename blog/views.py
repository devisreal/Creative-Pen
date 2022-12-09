from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm

@login_required
def create_post(request):
   if not request.user.is_author:
      messages.warning(request, 'You cannot perform that action')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:
      form = CreatePostForm()
      context = {
         'form': form
      }
      return render(request, 'blog/create_post.html', context)
