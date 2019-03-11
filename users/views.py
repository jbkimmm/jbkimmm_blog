from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, RegistrationForm
from .models import UserProfile

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('users:login')
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})
        # return render(request, '/base.html', )

@login_required
def profile(request, user=None):
    if user:
        obj = UserProfile.objects.get(user=request.user)
    else:
        #user = request.user
        obj = UserProfile.objects.get(user=request.user)
    args = {'obj': obj}
    return render(request, 'users/profile.html', args)

def view_profile(request, user=None):
    if user:
        obj = UserProfile.objects.get(user=request.user)
    else:
        #user = request.user
        obj = UserProfile.objects.get(user=request.user)
    args = {'obj': obj}
    return render(request, 'users/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            args = {'form': form}
            update_session_auth_hash(request, form.user)
            return render(request, 'users/profile.html', args)
        else:
            return render(request, 'users/change_password.html', args)
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'users/change_password.html', args)
