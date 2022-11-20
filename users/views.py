from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request, slug):   
   context = {}
   return render(request, 'users/dashboard.html', context)


@login_required
def user_profile(request, slug):
   context = {}
   return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request, slug):
   context = {}
   return render(request, 'users/edit_profile.html', context)


