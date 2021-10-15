from django.db import models
from django.shortcuts import redirect, render
from . import models
# Create your views here.

def readMakanan(req):
    if req.POST:
        input_jenis = req.POST["jenis"]
        input_nama = req.POST["nama"]
        input_harga = req.POST["harga"]
        models.makanan.objects.create(jenis = input_jenis, nama= input_nama, harga = input_harga)
    data = models.makanan.objects.all()
    return render(req, "makanan/index.html", {
        "data": data,
    })

def hapus(request, id):
    models.makanan.objects.filter(id=id).delete()
    return redirect('/')
def edit(request, id):
    if request. POST:
        input = request.POST[ "nama"]
        print(input)
        models.makanan.objects.filter(id = id).update(nama = input)
        return redirect('/')
    data = models.makanan.objects.filter(id = id).first()
    return render(request,"makanan/edit.html",{
       "detailData": data,
    })
def detail(request, id):
    data = models.makanan.objects.filter(id = id).first()
    print(data)
    return render(request,"makanan/detail.html",{
        "dataDetail": data
    })

