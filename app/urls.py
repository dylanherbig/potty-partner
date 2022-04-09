from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
    path('<int:pk>/test/', views.TestView.as_view(), name='test'),
]