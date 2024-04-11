from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from django.urls import reverse_lazy
from users.forms import CreationForm, AuthForm, EditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
def login_site(request):
    if request.user.is_authenticated:
        return redirect('profile') 
    else:
        form = AuthForm()
        if request.method == "POST":
            form = AuthForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                pw = form.cleaned_data.get('password')
                auth = authenticate(username = username, password = pw)
                if auth is not None:
                    login(request, auth)
                    return redirect('homepage')
                else:
                    return render(request, 'users/login.html', {"form" : form, "username" : form['username'], "password" : form['password']})
        return render(request, 'users/login.html', {"username" : form['username'], "password" : form['password']})

def signup(request):
    if request.method == "POST":
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'users/signup.html', {"form": form})
    else:
        form = CreationForm()
    return render(request, 'users/signup.html', {"form" : form, "first" : form['first_name'], "last" : form['last_name'], "username" : form['username'], "pw1": form['password1'], "pw2":form['password2']})

@login_required
def logout(request):
    return logout_then_login(request, login_url = reverse_lazy('login'))

@login_required
def edit_profile(request):
    profile = request.user
    if request.method == "POST":
        form = EditForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            return render(request, 'users/profile.html', {"form" : form, "first" : form['first_name'], "last" : form['last_name'], "username" : form['username'], "date_joined" : form['date_joined'], 'email':form['email']})
    else:
        form = EditForm(instance = profile)
    return render(request, 'users/profile.html', {"form" : form, "first" : form['first_name'], "last" : form['last_name'], "username" : form['username'], "date_joined" : form['date_joined'], 'email':form['email']})

class PasswordReset(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/pwreset.html'
    success_url = reverse_lazy('profile')