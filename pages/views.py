from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage
from account.models import User
from blog.models import PostCategory, Post
from .models import ContactDetail, Subscriber


def home(request):
   authors = User.objects.filter(is_author=True)   
   context = {
      'authors': authors,      
   }
   return render(request, 'pages/home.html', context)

def footer(request):
   if request.method == 'POST':      
      email = request.POST['email']      
      Subscriber.objects.create(email=email)
      
      messages.success(request, 'Thank you for subscribing! 👍')
      return redirect(request.META.get('HTTP_REFERER'))

def latest_posts(request):   
   try:
      posts = Post.objects.all().order_by('-date_posted')
   except Post.DoesNotExist:
      return redirect('error_page')   
   context = {
      'posts': posts
   }
   return render(request, 'pages/latest_posts.html', context)

def categories(request):      
   categories = PostCategory.objects.all()
   for category in categories:
      category_posts = Post.objects.distinct('category__name').order_by('category__name', '-date_posted')
   context = { 
      'categories': categories,
      'category_posts': category_posts
   }
   return render(request, 'pages/categories.html', context)

def single_category(request, slug):   
   try:
      category =  PostCategory.objects.get(slug=slug)
      category_posts = Post.objects.filter(category=category)
   except PostCategory.DoesNotExist:
      return redirect('error_page')
   context = {
      'category': category,   
      'category_posts': category_posts
   }
   return render(request, 'pages/single_category.html', context)

def about(request):
   categories = PostCategory.objects.all().order_by('name')
   p = Paginator(categories, 5)   
   page = request.GET.get('page')
   paginated_categories = p.get_page(page)   
   
   context = { 
      'paginated_categories': paginated_categories
   }
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
   context = { }
   return render(request, 'pages/contact.html', context)

def search_posts(request):
   if 'q' in request.GET:
      querystring = request.GET['q']      
      if querystring:
         post_results = Post.objects.filter(
            Q(post_title__icontains=querystring) |
            Q(post_author__username__icontains=querystring) |
            Q(post_type__icontains=querystring) |
            Q(category__name__icontains=querystring) |
            Q(slug__icontains=querystring)
         )

         author_results = User.objects.filter(is_author=True).filter(
            Q(username__icontains=querystring) |
            Q(first_name__icontains=querystring) |
            Q(last_name__icontains=querystring) |
            Q(slug__icontains=querystring)
         ).annotate(posts_count=Count('post')).order_by('first_name')
         #  !categories = PostCategory.objects.annotate(posts_count=Count('post')).all().order_by('name')   
         
         readers_results = User.objects.filter(is_author=False).filter(
            Q(username__icontains=querystring) |
            Q(first_name__icontains=querystring) |
            Q(last_name__icontains=querystring) |
            Q(slug__icontains=querystring)
         ).order_by('first_name')

         categories_result = PostCategory.objects.filter(
            Q(name__icontains=querystring) |            
            Q(slug__icontains=querystring)
         )
         
         context = {
            'querystring': querystring,
            'post_results': post_results,
            'author_results': author_results,
            'readers_results': readers_results,
            'categories_result': categories_result,
            'search_count': post_results.count() + author_results.count() + readers_results.count() + categories_result.count()
         }
         return render(request, 'pages/post_results.html', context)         
      else:
         messages.error(request, 'Please enter a search item!')
         return redirect(request.META.get("HTTP_REFERER"))    
      
   else:      
      messages.error(request, 'Please enter a search item!')
      return render(request,'pages/post_results.html')  

def _error_page(request):
   return render(request, 'pages/404.html')
