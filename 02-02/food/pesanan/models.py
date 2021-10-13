from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from makanan.models import makanan
from minuman.models import minuman
# Create your models here.
class pesanan(models.Model):
    makanan = models.ForeignKey(makanan, on_delete=models.CASCADE)
    jumlah_makanan = IntegerField()
    minuman = models.ForeignKey(minuman, on_delete=models.CASCADE)
    jumlah_minuman = models.IntegerField()
