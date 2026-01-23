from django import forms

# The comment `The class ContactFormForm defines a form with fields for customer email, name, and
# message in a Python Django application` is providing a brief description or summary of the purpose
# of the `ContactFormForm` class. It explains that the class is defining a form that will have fields
# for customer email, name, and message within a Python Django application. This comment helps
# developers understand the intent and functionality of the class at a high level.



class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='  Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')


class ContactoEmpresaForm(forms.Form):
    name_empresa = forms.CharField(max_length=64, label='Nombre')
    email_empresa = forms.EmailField(label='  Correo')
    phone_empresa = forms.CharField(max_length=10, label='Telefono')
    message_empresa = forms.CharField(widget=forms.Textarea, label='Mensaje')
    