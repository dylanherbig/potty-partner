#from django.conf.urls import url   
from django.urls import include, re_path                                                                                                                           
from . import views


urlpatterns = [ 
    #url(r'', views.default_map, name="default"),
    re_path(r'', views.default_map, name="default"),
]

