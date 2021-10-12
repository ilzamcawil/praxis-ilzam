from django.urls import path

from . import views

urlpatterns = [
    path('', views.readMinuman, name='readMinuman'),
    path('minuman/', views.readMinuman, name='readMinuman'),
    path('hapus/<id>',views.hapus),
    path('edit/<id>/', views.edit),
    path('detail/<id>/', views.detail),

]