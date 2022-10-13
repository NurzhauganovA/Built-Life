from django.contrib import auth
from django.shortcuts import render, redirect


def RegisterUser(request):

    context = {}

    return render(request, 'account/sign-up.html', context)


def LoginUser(request):

    context = {}

    return render(request, 'account/sign-in.html', context)


def LogoutUser(request):
    auth.logout(request)
    return redirect('/')