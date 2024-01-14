from django import forms
from . import models

class ProductosForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"


class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = models.Proveedor
        fields = "__all__"