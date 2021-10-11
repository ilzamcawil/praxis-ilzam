from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index),
    path('hapus/<id>/', views.hapus),
    path('detail/<id>/', views.detail),
    path('edit/<id>/'