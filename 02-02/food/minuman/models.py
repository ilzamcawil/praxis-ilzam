from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class minuman(models.Model):
    jenis = models.CharField(max_length=255)
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()
