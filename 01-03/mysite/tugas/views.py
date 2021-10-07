# from django.db import models
from django.db.models.fields.json import DataContains
from django.shortcuts import render
from . import models

# Create your views here.
# def index(request):
#     if request_POST:
#         input = request.POST["nama"]
#         input = tugas.objects.create("nama=input")
#         print(input)
from django.http import HttpResponse


def index(request):
    if request.POST:
        #input ke database
        models.tugas.objects.create(nama=request.POST['nama'])
    #nampilin data
    data2 = models.tugas.objects.all()
    return render(request, 'index.html', {'isi': data2})
def about(request):
    return HttpResponse("halaman about")
