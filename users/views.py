from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password')
            auth = authenticate(username = username, password = pw)
            if auth is not None:
                login(request, auth)
                return redirect('homepage')
    return render(request, 'users/login.html', {"form": form})