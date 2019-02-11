"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from classroom.views import users, volunteers, NGOs, companies

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/volunteer/', students.VolunteerSignUpView.as_view(), name='volunteer_signup'),
    path('accounts/signup/NGO/', teachers.NGOSignUpView.as_view(), name='NGO_signup'),
    path('accounts/signup/company/', students.CompanySignUpView.as_view(), name='company_signup'),
]
