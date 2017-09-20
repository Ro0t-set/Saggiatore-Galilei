from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

class Categoria(models.Model):
    categorie = models.CharField(max_length=100)

    def __str__(self):
        return self.categorie

class Articolo(models.Model):
    author = models.ForeignKey('auth.User')
    categorie = models.ForeignKey('Categoria')
    titolo = models.CharField(max_length=100)
    text = models.TextField()
    convalida= models.BooleanField(default=False)

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titolo
    class Meta:
        ordering = ["-published_date"]
