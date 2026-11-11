from django import forms
from .models import Producto


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu nombre"}),
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "nombre@ejemplo.com"}),
    )
    telefono = forms.CharField(
        label="Teléfono (opcional)",
        required=False,
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu teléfono"}),
    )
    asunto = forms.CharField(
        label="Asunto",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Asunto del mensaje"}),
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Escribí tu consulta"}),
    )


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "stock", "marca", "categoria", "imagen", "activo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "min": "0"}),
            "stock": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
