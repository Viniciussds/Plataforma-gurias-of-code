from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse('Usuario já existe')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.set_password(password1)
                user.save()
                return redirect('login')
    return  render(request,'register.html')

def loginPage(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                     login(request,user)
                     return redirect('home')
            else:
                 return HttpResponse('Usuário ou senha inválidos')
    return render(request,'login.html')


def logoutPage(request):
    logout(request)
    return redirect('home')