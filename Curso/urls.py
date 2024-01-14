from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos", views.productos, name="productos"),
    path("productos/form", views.productos_form, name="productos_form"),
    path("proveedores", views.proveedores, name="proveedores"),
    path("proveedores/form", views.proveedores_form, name="proveedores_form"),
    path("categoria", views.categoria, name="categoria")

]
