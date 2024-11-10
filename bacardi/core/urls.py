from django.urls import path
from . import views

urlpatterns = [
    path('step1/', views.seleccion_pais, name='seleccion_pais'),
    path('step2/', views.step2, name='step2'),
]
