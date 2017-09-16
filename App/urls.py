from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.lista_articoli, name='lista_articoli'),
    url(r'^pubblica/$', views.pubblica, name='pubblica'),
    url(r'^login/$', login, name='login'),
]
