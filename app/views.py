from re import template
from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'app/login.html'


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1Ijoic2pvc2hpMTIyNSIsImEiOiJjbDFzOW9yMzcwcHN6M2NzNnF0bXRxOGdpIn0.dZv1B-VUgqjbPp__sRW8FA'
    return render(request, 'login.html', 
                  { 'mapbox_access_token': mapbox_access_token })