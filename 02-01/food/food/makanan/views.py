from django.shortcuts import render
from . import models
# Create your views here.
def readmakan(req):
    if req.POST:
        data = request.POST['nama']
        print(data)
        #input ke database
        input_jenis = req.POST["jenis"]
        input_nama = req.POST["nama"]
        input_harga = req.POST["harga"]
        models.makanan.objects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.makanan.objects.all()
    return render(req, "makanan/index.html",{
        "data": data,
    })
