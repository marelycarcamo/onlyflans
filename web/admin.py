from django.contrib import admin


# Aquí se registra el modelo Flan
from .models import Flan
admin.site.register(Flan) 

# Aquí se registra el modelo ContactForm
from .models import ContactForm
admin.site.register(ContactForm)

#Registro del modelo Cafe
from .models import Cafe
admin.site.register(Cafe)

#Registro del modelo Dulce
from .models import Dulce
admin.site.register(Dulce)

from .models import ContactoEmpresa
admin.site.register(ContactoEmpresa)




