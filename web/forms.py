from django import forms

# The class ContactFormForm defines a form with fields for customer email, name, and message in a
# Python Django application.
class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='  Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')
