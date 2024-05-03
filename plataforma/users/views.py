from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def singUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Nome de usuário já existe')
                return redirect('singup')
            else:
                user = User.objects.create_user(username,email,pass1)
                user = user.save()
                return redirect('login')
    return render(request, 'singup.html')



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Nome de usuário ou senha incorretos')
    return render(request, 'login.html')
    
@login_required
def logoutPage(request):
    logout(request)
    return redirect('home')

