from django.urls import path

from . import views

urlpatterns = [
    path('', views.readMakanan, name='readMakanan'),
    path('hapus/<id>/',views.hapus),
    path('edit/<id>/', views.edit),
    path('detail/<id>/', views.detail),

]