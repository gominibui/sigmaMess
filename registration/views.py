from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm
from .models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def success(request):
    return render(request, "succces_reg/success.html")

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, 'Ваш аккаунт отключен.')
                    return redirect('login')
            else:
                messages.error(request, 'Неправильный логин или пароль.')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'registration/index.html', {'login_form': form, 'register_form': UserRegistrationForm()})    

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'succces_reg/success.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/index.html', {'register_form': user_form, 'login_form': LoginForm()})


@login_required
def dashboard(request):
    return render(request, 'test.html/test.html')
    
@login_required
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')  # Redirect to the login page or homepage after logout
    return render(request, 'logout/logout.html')