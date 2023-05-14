from django.urls import path
from . import views

urlpatterns = [
    path('', views.autorizacao, name="autorizacao"),
    path('atualiza_autorizacao/', views.att_autorizacao, name="atualiza_autorizacao"),
    path('update_autorizacao/<int:id>', views.update_autorizacao, name="update_autorizacao")
]
