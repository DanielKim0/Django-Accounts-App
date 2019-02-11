from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from ..forms import NGOSignUpForm
from ..models import User

class NGOSignUpView(CreateView):
    form_class = NGOSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
