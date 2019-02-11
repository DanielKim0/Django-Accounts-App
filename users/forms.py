# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class VolunteerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 1
        if commit:
            user.save()
        volunteer = Volunteer.objects.create(user=user)
        return user

class NGOCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        if commit:
            user.save()
        ngo = NGO.objects.create(user=user)
        return user

class CompanyCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 3
        if commit:
            user.save()
        company = Company.objects.create(user=user)
        return user
