from django import forms


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