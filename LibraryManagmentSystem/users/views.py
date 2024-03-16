from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm()
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form": form})

def profile(request):
    return render(request, 'users/profile.html')