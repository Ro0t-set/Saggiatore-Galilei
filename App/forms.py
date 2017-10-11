from django import forms
from django.db import models
from django.forms import formset_factory
from django.utils import timezone
import re
from django.forms import BaseModelFormSet
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Articolo



class ArticoloForm(forms.ModelForm):
    class Meta:
        model = Articolo
        fields = ['categorie', 'titolo', 'text','foto' ]


class CercaArticoli(forms.Form):
    q = forms.CharField(label='nome', max_length="100")
    #autore = forms.ModelChoiceField(queryset=User.objects.all())

class Mail(forms.Form):
    testo=forms.CharField(label='testo', max_length="1000")
    mail= forms.EmailField(label='mail', max_length="100")
