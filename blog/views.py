from django.shortcuts import render


# Create your views here.
def home(request):
   context = {}
   return render(request, 'blog/home.html', context)

def about(request):
   context = {}
   return render(request, 'extras/about.html', context)

def contact(request):
   context = {}
   return render(request, 'extras/contact.html')