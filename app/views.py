from re import template
from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from app.forms import ToiletForm
from app.models import Toilet

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'app/login.html'


class AboutView(generic.TemplateView):
    template_name = 'app/about.html'


@login_required(login_url='/accounts/google/login')
def create_toilet(request):
    if request.method == 'POST':
        form = ToiletForm(request.POST)
        if form.is_valid():
            t = Toilet(longitude = form.cleaned_data['longitude'],
                latitude = form.cleaned_data['latitude'],
                title = form.cleaned_data['title'],
                author = request.user,)
            t.save()
            return HttpResponseRedirect('/')
    else:
        form = ToiletForm()
    return render(request, 'app/create-toilet.html', {'form': form})