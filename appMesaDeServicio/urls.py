from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("login/",views.login),
    path("administrador/",views.inicioAdministrador),
    path("tecnico/",views.inicioTecnico),
    path("empleado/",views.inicioEmpleado),
    path("vistaSolicitud/",views.vistaSolicitud),
    path("registroSolicitud/", views.registrarSolicitud),
    path("listarCasos/",views.listarCasos),
    path("asignarTecnicoCaso/",views.asignarTecnicoCaso),
    path("salir/",views.salir),
]