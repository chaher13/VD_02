from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from utilisateur.forms import  UserLoginForm, UserRegistrationForm


def index(request):
    return render(request, "registration/index.html")

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'registration/deconnexion.html')

@login_required
def user_dashboard(request):
    user = request.user
    return render(request, 'registration/user_dashboard.html', {'user': user})
