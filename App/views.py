from django.shortcuts import render
from django.utils import timezone
from .models import Articolo, Categoria
from .forms import ArticoloForm, CercaArticoli, FiltroAutore
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
import operator
from django.forms import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@csrf_protect

def lista_articoli(request):
    articoli =  Articolo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    form = CercaArticoli(request.GET)
    if form.is_valid():
        articoli = articoli.filter(titolo=form.cleaned_data["q"])
        articoli = articoli.filter(titolo= form.cleaned_data["autore"])

    return render(request, 'articoli/lista_articoli.html', {'articoli' : articoli, 'form' : form})

@login_required(login_url='/login/')
def pubblica(request):
    if request.method == "POST":
        form = ArticoloForm(request.POST)
        if form.is_valid():
            articolo = form.save(commit=False)
            articolo.author = request.user
            articolo.published_date = timezone.now()
            articolo.save()
            return redirect('/')
    else:
        form = ArticoloForm()
    return render(request, 'articoli/pubblica.html', {'form': form})
