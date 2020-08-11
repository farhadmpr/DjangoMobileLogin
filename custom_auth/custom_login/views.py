from typing import Optional
from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MyUser
from . import forms, helper


def register(request):
    form = forms.RegisterForm()

    if request.method == "POST":
        try:
            if "mobile" in request.POST:
                mobile = request.POST.get('mobile')
                user = MyUser.objects.get(mobile=mobile)
                otp = helper.get_random_otp()
                #helper.send_otp(mobile, otp)
                user.otp = otp
                user.save()
                return HttpResponseRedirect(reverse('verify'))
        except MyUser.DoesNotExist:
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                otp = helper.get_random_otp()
                #helper.send_otp(mobile, otp)
                user.otp = otp
                user.save()
                return HttpResponseRedirect(reverse('verify'))
    return render(request, 'register.html', {'form': form})


def verify(request):
    pass


def mobile_login(request):
    if request.method == "POST":
        if "mobile" in request.POST:
            mobile = request.POST.get('mobile')
            user = MyUser.objects.get(mobile=mobile)
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'mobile_login.html')


def dashboard(request):
    return render(request, 'dashboard.html')
