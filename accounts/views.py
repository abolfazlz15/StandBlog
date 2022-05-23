from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserEditForm, RegisterForm, LoginForm


# login view code
def loginView(request):
    if request.user.is_authenticated:  # The logged in user does not have access to the login page
        return redirect('home:home')
    # for login
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', context={'form': form})


# register view code
def registerView(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    return render(request, 'accounts/singup.html', context={'form': form})


def userProfileEdit(request):
    if not request.user.is_authenticated:  # The logged in user does not have access to the login page
        return redirect('accounts:login')
    form = UserEditForm(instance=request.user)
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'accounts/user_profile_edit.html', context={'form': form})


# logout view code
def logoutView(request):
    logout(request)
    return redirect('home:home')

