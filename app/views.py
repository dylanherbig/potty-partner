from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.


def IndexView(request):
    return HttpResponse("Hello world! We are the team behind Potty Partner :))")