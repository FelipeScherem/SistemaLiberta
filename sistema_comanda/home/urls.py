from django.urls import path
from . import views

urlpatterns = [
    #1  é a url;        busca def           3 sei la
    path(""         ,   views.login     ,   name="login"    ),
    path("pedidos"  ,   views.pedidos   ,   name="pedidos"  ),
    path("graficos" ,   views.charts    ,   name="graficos" ),
    path("clientes" ,   views.clientes  ,   name="clientes" ),
    path("produtos" ,   views.produtos  ,   name="produtos" ),
]
