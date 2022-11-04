from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from account.models import User
from django.contrib import messages


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')
    else:
        if request.method == 'POST':
            username_or_email = request.POST['username_or_email']
            password = request.POST['password']

            if User.objects.filter(username=username_or_email).exists():
                username = username_or_email
            elif User.objects.filter(email=username_or_email).exists():
                username = User.objects.get(email=username_or_email).username
            else:
                username = None

            if username is not None:
                try:
                    user = authenticate(username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, "You are successfully logged in.")
                    return redirect('home')
                except:
                    messages.error(request, "Incorrect password.")
                    return redirect('login')
            else:
                messages.error(request, "Enter correct details.")
                return redirect('login')    
    return render(request, 'account/login.html')

def register(request):
    context = {}
    return render(request, 'account/register.html', context)

@login_required
def user_logout(request):    
    logout(request)
    # Return success message
    messages.success(request, 'See you soon! 👋')
    return redirect(request.META.get('HTTP_REFERER'))
    # return redirect('login')