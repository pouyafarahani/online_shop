from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreateFrom


class SignupView(CreateView):
    form_class = CustomUserCreateFrom
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

