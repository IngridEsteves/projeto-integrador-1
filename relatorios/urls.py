from django.urls import path
from . import views

urlpatterns = [
    path('novo_relatorio/', views.novo_relatorio, name="novo_relatorio"),
    path('listar_relatorio/', views.listar_relatorio, name="listar_relatorio"),
    path('relatorio/<str:identificador>/', views.relatorio, name="relatorio"),
]
