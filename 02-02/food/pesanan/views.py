from django.shortcuts import render, redirect
from . import models

# Create your views here.
def readPesanan(req):
    if req.POST:
        get_makanan = req.POST["makanan"]
        get_minuman = req.POST["minuman"]
        get_jumlah_makanan = req.POST["jumlah_makanan"]
        get_jumlah_minuman= req.POST["jumlah_minuman"]

        input_makanan = models.makanan.objects.filter(id=get_makanan).first()
        input_minuman = models.minuman.objects.filter(id=get_minuman).first()
        models.pesanan.objects.create(makanan = input_makanan, minuman = input_minuman, jumlah_makanan=get_jumlah_makanan,jumlah_minuman=get_jumlah_minuman)
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    return render(req, "pesanan/index.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data": data,
    })
def hapus(request, id):
    models.pesanan.objects.filter(id=id).delete()
    return redirect('/pesanan/')
def edit(request, id):
    if request. POST:
        input = request.POST[ "nama"]
        print(input)
        models.pesanan.objects.filter(id = id).update(nama = input)
        return redirect('/')
    data = models.pesanan.objects.filter(id = id).first()
    return render(request,"pesanan/edit.html",{
       "detailData": data,
    })
def detail(request, id):
    data = models.pesanan.objects.filter(id = id).first()
    print(data)
    return render(request,"pesanan/detail.html",{
        "detail.data": data
    })
