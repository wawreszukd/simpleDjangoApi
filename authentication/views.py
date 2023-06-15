from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def handleLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        loginUser = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=loginUser, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'user or password is incorrect')


    context = {'title': 'login', 'authcheck': request.user.is_authenticated}
    return render(request,'loginPage.html',context=context)

def handleRegister(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'succesfully created')
            return redirect('login')
    context = {'title': 'register', 'form': form, 'authcheck': request.user.is_authenticated}
    return render(request,'registerPage.html',context=context)
def handleLogOut(request):
    logout(request)
    return redirect('login')