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
      if request.method == "POST":
         create_post_form = CreatePostForm(request.POST, request.FILES)
         if create_post_form.is_valid():
            instance = create_post_form.save(commit=False)
            instance.post_author = request.user
            instance.save()
            create_post_form.save_m2m()
         else:
            messages.error(request, f"An error occured")
            return redirect('blog:create_post')
      else:
         create_post_form = CreatePostForm()
      context = {
         'create_post_form': create_post_form,         
      }
      return render(request, 'blog/create_post.html', context)
