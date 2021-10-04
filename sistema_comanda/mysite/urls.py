from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #quando recebe("caminho")
    path('', include('home.urls')),
    path('login', include('home.urls')),
    path('graficos', include('home.urls')),
]