from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import CustomUser, UserProfile


def RegisterUser(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('repeat_password')

        if password1 == password2:
            user = CustomUser.objects.create_user(username=username, password=password1)
            user.save()
            new_user = authenticate(
                                    username=username,
                                    password=password1
                                    )
            login(request, new_user)
            print('User created')
        else:
            print('User not created')
            messages.info(request, 'Password not matching')
            return redirect('/account/sign-up')
        return redirect('/')

    return render(request, 'account/sign-up.html')


def LoginUser(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(
                                username=username,
                                password=password
                                )
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('account/sign-in')

    return render(request, 'account/sign-in.html')


def LogoutUser(request):
    auth.logout(request)
    return redirect('/')