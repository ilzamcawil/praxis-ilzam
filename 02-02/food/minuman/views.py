from django.shortcuts import render, redirect
from . import models

# Create your views here.
def readMinuman(req):
    if req.POST:
        input_jenis = req.POST["jenis"]
        input_nama = req.POST["nama"]
        input_harga = req.POST["harga"]
        models.minuman.objects.create(jenis = input_jenis, nama= input_nama, harga = input_harga)
    data = models.minuman.objects.all()
    return render(req, "minuman/index.html", {
        "data": data,
    })
def hapus(request, id):
    models.minuman.objects.filter(id=id).delete()
    return redirect('/minuman/')
def edit(request, id):
    if request. POST:
        input = request.POST[ "nama"]
        print(input)
        models.minuman.objects.filter(id = id).update(nama = input)
        return redirect('/')
    data = models.minuman.objects.filter(id = id).first()
    return render(request,"minuman/edit.html",{
       "detailData": data,
    })
def detail(request, id):
    data = models.minuman.objects.filter(id = id).first()
    print(data)
    return render(request,"minuman/detail.html",{
        "detail.data": data
    })
