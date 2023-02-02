from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from hitcount.views import HitCountDetailView
from .forms import CommentForm, CreatePostForm
from .models import Post


def single_post(request, slug):
   try:
      post = Post.objects.get(slug=slug)
   except Post.DoesNotExist:
      return redirect('error_page')
   context = {
      'post': post
   }
   return render(request, 'blog/single_post.html', context)

@login_required
def edit_post(request, slug):
   post = Post.objects.get(slug=slug)

   if request.user != post.post_author:
      messages.error(request, 'You are not allowed to edit this post')
      return redirect('blog:single_post', slug=post.slug)
   else:
      if request.method == "POST":         
         edit_post_form = CreatePostForm(request.POST or None, request.FILES, instance=post)
         if edit_post_form.is_valid():
            edit_post_form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('blog:single_post', slug=post.slug)
         else:
            messages.error(request, f"An error occured")
            return redirect('new_post')
      else:
         edit_post_form = CreatePostForm(instance=post)
      context = {
         'post': post,
         'edit_post_form': edit_post_form
      }
      return render(request, 'blog/edit_post.html', context)    
   

@login_required()
def delete_post(request, slug):
   post = Post.objects.get(slug=slug)

   if request.user != post.post_author:
      messages.error(request, 'You are not allowed to delete this post')
      return redirect('blog:single_post', slug=post.slug)
   else:      
      post.delete()
      messages.success(request, 'Post deleted successfully')
      return redirect('latest_posts')


class PostDetailView(HitCountDetailView, View):
   model = Post
   form_class = CommentForm()
   template_name = 'blog/single_post.html'
   context_object_name = 'post'
   slug_field = 'slug'
   # set to True to count the hit
   count_hit = True

   def get_context_data(self, **kwargs):
      context = super(PostDetailView, self).get_context_data(**kwargs)
      context.update({
         'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
      })
      return context
   
   def get(self, request, slug, *args, **kwargs):
      post = Post.objects.get(slug=slug)
      form = CommentForm()      

      context = {
         'post': post,
         'form': form,         
      }

      return render(request, 'blog/single_post.html', context)

   def post(self, request, slug, *args, **kwargs):
      post = Post.objects.get(slug=slug)
      form = CommentForm(request.POST)    

      if form.is_valid():
         new_comment = form.save(commit=False)
         new_comment.author = request.user
         new_comment.post = post
         new_comment.save()
         messages.success(request, 'New comment added')
         return redirect('blog:single_post', slug=post.slug)
      else:
         messages.error(request, 'An error occured')
         return redirect('blog:single_post', slug=post.slug)

      context = {
         'post': post,
         'form': form,         
      }
      return render(request, 'blog/single_post.html', context)
         
      



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

            messages.success(request, f"New post created")
            return redirect('home')
         else:
            messages.error(request, f"An error occured")
            return redirect('new_post')
      else:
         create_post_form = CreatePostForm()
      context = {
         'create_post_form': create_post_form,         
      }
      return render(request, 'blog/create_post.html', context)

