from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)
    

class ProfilePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'profile.html', context=None)


class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)
    
class RegisterPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'register/index.html', context=None)
    