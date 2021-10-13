from django.urls import path

from . import views

urlpatterns = [
    path('', views.readPesanan, name='readPesanan'),
    path('minuman/', views.readPesanan, name='readPesanan'),
    path('hapus/<id>',views.hapus),
    path('edit/<id>/', views.edit),
    path('detail/<id>/', views.detail),

]