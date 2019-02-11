from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from ..forms import VolunteerSignUpForm
from ..models import User

class VolunteerSignUpView(CreateView):
    template_name = 'signup.html'
    form_class = VolunteerSignUpForm
    success_url = reverse_lazy('login')
