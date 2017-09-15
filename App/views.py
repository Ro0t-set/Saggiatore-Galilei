from django.shortcuts import render
from django.utils import timezone
from .models import Articolo, Categoria

def lista_articoli(request):
    articoli =  Articolo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articoli/lista_articoli.html', {'articoli' : articoli})
