from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User


class AuthView(ListView):
    user = User
    template_name = 'social_networks/auth.html'


