from django.urls import path
from  proveedores_app import views


urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),
    path('registrar/',views.registrar,name='registrar'),
    path('seleccionar/<codigo>',views.seleccionar,name='seleccionar'),
    path('editar/',views.editar,name='editar'),
    path('borrar/<codigo>',views.borrar,name='borrar')
]