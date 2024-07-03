from django import forms

# The class ContactFormForm defines a form with fields for customer email, name, and message in a
# Python Django application.
class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='  Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')



    # class ContactCompanyFormForm(forms.Form):
    #     email_company = forms.EmailField(label='  Correo')
    #     name_company = forms.CharField(max_length=64, label='Nombre')
    #     phone_compay = forms.CharField(max_length=10, label='Telefono')
    #     message_company = forms.CharField(widget=forms.Textarea, label='Mensaje')
