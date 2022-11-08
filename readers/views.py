from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request, slug):   
   context = {}
   return render(request, 'readers/dashboard.html', context)