from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from ..forms import CompanySignUpForm
from ..models import User

class CompanySignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CompanySignUpForm
    success_url = reverse_lazy('login')
