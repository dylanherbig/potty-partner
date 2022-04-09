from re import template
from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'app/login.html'
