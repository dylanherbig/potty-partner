from re import template
from django.shortcuts import render, HttpResponse
from django.views import generic

from app.models import Toilet

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'app/login.html'

class AboutView(generic.TemplateView):
    template_name = 'app/about.html'

class TestView(generic.DetailView):
    template_name = 'app/test.html'
    model = Toilet

