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
        fields = ['categorie', 'titolo', 'text', ]


class CercaArticoli(forms.Form):
    q = forms.CharField(label='nome', max_length="100")
    #autore = forms.ModelChoiceField(queryset=User.objects.all())
