from django.shortcuts import render
from django.utils import timezone
from .models import Articolo, Categoria
from .forms import ArticoloForm, CercaArticoli, Mail
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
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator



@csrf_protect

def lista_articoli(request):
    articoli =  Articolo.objects.filter(convalida = True)
    categorie = Categoria.objects.all()
    autori = User.objects.all()
    form = CercaArticoli(request.GET)
    cerca = request.GET.get("q")
    filtro_categoria= request.GET.get("c")
    filtro_autori= request.GET.get("a")
    if form.is_valid():
        articoli = articoli.filter(Q(titolo__icontains=cerca)|
                                    Q(text__icontains=cerca))
    if filtro_categoria:
        articoli = articoli.filter(Q(categorie__categorie__exact=filtro_categoria))

    if filtro_autori:
        articoli = articoli.filter(Q(author__articoli=filtro_autori))



    paginator = Paginator(articoli, 3)
    page = request.GET.get('page')
    try:
        articoli = paginator.page(page)
    except PageNotAnInteger:
        articoli = paginator.page(1)
    except EmptyPage:
        articoli = paginator.page(paginator.num_pages)

    return render(request, 'articoli/lista_articoli.html', {'articoli' : articoli, 'form' : form, 'categorie': categorie, 'autori':autori})

def vedi_tutto(request):
    articoli =  Articolo.objects.all()
    articoli = request.GET.get("q")
    if articoli:
        articoli = Articolo.objects.filter(titolo= articoli)
        return render(request, 'articoli/vedi_tutto.html', {'articoli' : articoli})


@login_required(login_url='/login/')
def pubblica(request):
    if request.method == "POST":
        form = ArticoloForm(request.POST, request.FILES)
        if form.is_valid():
            articolo = form.save(commit=False)
            articolo.author = request.user
            articolo.published_date = timezone.now()
            articolo.save()
            print ("pubblicazione avvenuta con succcesso")
            return redirect('/')
    else:
        form = ArticoloForm()
    return render(request, 'articoli/pubblica.html', {'form': form})


def scrivici(request):
    if request.method == "POST":
        form = Mail(request.POST)
        if form.is_valid():
            subject, from_email, to = form.cleaned_data['mail'], 'mail', 'mail'
            text_content = '456'
            html_content =  form.cleaned_data['testo']
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send(fail_silently=False)
    else:
        form = Mail()
    return render(request, 'articoli/scrivici.html', {'form': form})
