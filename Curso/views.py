from django.shortcuts import render, redirect
from . import models
from . import forms


def index(request):
    return render(request, "Curso/index.html")


def productos(request):
    consulta=models.Producto.objects.all()
    contexto={"productos": consulta}
    return render(request, "Curso/productos.html", contexto)

def productos_form(request):
    if request.method == "POST":
        form= forms.ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos")
    else: 
        form = forms.ProductosForm()
    return render(request, "Curso/productos_form.html", {"form": form})

def proveedores(request):
    consulta=models.Proveedor.objects.all()
    contexto={"proveedores": consulta}
    return render(request, "Curso/proveedores.html", contexto)

def proveedores_form(request):
    if request.method == "POST":
        form= forms.ProveedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proveedores")
    else: 
        form = forms.ProveedoresForm()
    return render(request, "Curso/proveedores_form.html", {"form": form})


def categoria(request):
    consulta=models.Categoria.objects.all()
    contexto={"Categoria": consulta}
    return render(request, "Curso/categoria.html", contexto)