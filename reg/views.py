from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import (
    User,
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth.decorators import login_required
from .forms import UserForm, CustomUserForm
from django.shortcuts import render, redirect


class RegisterForm(FormView):
    form_class = UserForm
    success_url = '/reg/profile'
    template_name = 'reg/reg.html'
    def form_valid(self, form):
        form.save()
        return super(RegisterForm, self).form_valid(form)

class ProfileForm(FormView):
    form_class = CustomUserForm
    success_url = '/'
    template_name = 'reg/reg.html'
    def form_valid(self, form):
        form.save()
        return super(ProfileForm, self).form_valid(form)

class AuthForm(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = "reg/reg.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(AuthForm, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

#
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
#
@login_required(login_url='/reg/login/')
def check(request):
    return HttpResponse("Checked!")

@login_required(login_url='/reg/login/')
def update_profile(request):
    user = request.user
    print (user)
    return HttpResponse("Checked!")