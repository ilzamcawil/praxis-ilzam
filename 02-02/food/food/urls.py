from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('makanan.urls')),
    path('minuman/', include('minuman.urls')),
    path('admin/', admin.site.urls),
]
