from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(req):
    # Check to see if logging in
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        # Authenticate
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req, "You have been logged in successfully!")
            return redirect('home')
        else:
            messages.success(req, "There was an error trying to login...")
            return redirect('home')

    return render(req, 'home.html', {})


def login_user(req):
    pass


def logout_user(req):
    logout(req)
    messages.success(req, "You have been logged out...")
    return redirect('home')

def register_user(req):
    return render(req, 'register.html')
