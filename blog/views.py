from django.shortcuts import render



def create_post(request):
   context = {}
   return render(request, 'blog/create_post.html', context)
