from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from .models import User

import base64
from django.core.files.base import ContentFile

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)

    else:
        form = LoginForm()

    return render(request, "users/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect("users:login")


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            nick_name = form.cleaned_data['nick_name']
            date_of_birth = form.cleaned_data['date_of_birth']

            data = request.POST['profile_img']

            img_fmt, img_str = data.split(';base64,')
            ext = img_fmt.split('/')[-1]
            profile_img = ContentFile(base64.b64decode(img_str), name='profile.' + ext)

            user = User.objects.create_user(email, password, nick_name, date_of_birth, profile_img)

            return redirect("users:login")

    else:
        form = SignupForm()

    return render(request, "users/signup.html", {'form': form})
    