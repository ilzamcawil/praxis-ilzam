# from django.db import models
from django.db.models.fields.json import DataContains
from django.shortcuts import render
from django.shortcuts import redirect, render
from . import models

# Create your views here.
# def index(request):
#     if request_POST:
#         input = request.POST["nama"]
#         input = tugas.objects.create("nama=input")
#         print(input)
#Create your views here.

from django.http import HttpResponse


def index(request):
    if request.POST:
        data = request.POST['nama']
        print(data)
        #input ke database
        models.tugas.objects.create(nama=request.POST['nama'])
        models.tugas.objects.create(nama = data)
    #nampilin data
    data2 = models.tugas.objects.all()
    return render(request, 'index.html', {'isi': data2})
def about(request):
    return HttpResponse("halaman about")
    return render (request, 'index.html', {'isi': data2})

def hapus(request, id):
    models.tugas.objects.filter(id = id).delete()
    return redirect('/')

def detail(request, id):
    data = models.tugas.objects.filter(id = id).first()
    print(data)
    return render(request,"detail.html",{
        "detail.data": data
    })
def edit(request, id):
    if request. POST:
        input = request.POST[ "nama"]
        print(input)
        models.tugas.objects.filter(id = id).update(nama = input)
        return redirect('/')
    data = models.tugas.objects.filter(id = id).first()
    return render(request,"edit.html",{
       "detailData": data,
    })
