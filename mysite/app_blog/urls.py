# app_blog/urls.py
from django.urls import path
from app_blog import views
urlpatterns = [
    path(r'', views.HomePageView.as_view()),
    path(r'', views.ProfilePageView.as_view()),
    path(r'', views.LoginPageView.as_view()),
    path(r'', views.RegisterPageView.as_view()),
]
