from django.contrib import admin
from .models import Flan
from .models import ContactForm

# Aquí se registra el modelo Flan
admin.site.register(Flan) 

# Aquí se registra el modelo ContactForm
admin.site.register(ContactForm)


