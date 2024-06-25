from django.shortcuts import render

# def index(request):
#   return render(request, 'index.html')

# def about(request):
#   return render(request, 'about.html')

# def welcome(request):
#   return render(request, 'welcome.html')



from django.http import HttpResponse
from django.template import loader

from web.forms import ContactFormForm

from .models import ContactForm, Flan

# def index(request):
#    flanes = Flan.objects.all()
#    template = loader.get_template('index.html')
#    context = {'flanes': flanes,}
#    return HttpResponse(template.render())


def index(request):
    flanes = Flan.objects.all()  # Obtener todos los objetos Flan
    context = {'flanes': flanes}  # Crear un diccionario de contexto
    return render(request, 'index.html', context)  # Pasar el contexto a la plantilla


def about(request):
# The code snippet `template = loader.get_template('about.html')` is loading the template file named
# 'about.html' using Django's template loader. This function retrieves the template object associated
# with the specified template name.
  template = loader.get_template('about.html')
  return HttpResponse(template.render())


def welcome(request):
  template = loader.get_template('welcome.html')
  return HttpResponse(template.render())

# def contacto(request):
#   template = loader.get_template('contacto.html')
#   return HttpResponse(template.render())


def base(request):
    return render(request, 'base.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Aquí guardar los datos del formulario en la base de datos
            ContactForm.objects.create(
                customer_email=form.cleaned_data['customer_email'],
                customer_name=form.cleaned_data['customer_name'],
                message=form.cleaned_data['message']
            )
            # Redirigir a una página de éxito o mostrar un mensaje
            return render(request, 'contacto_success.html')
            # return HttpResponseRedirect('/')
    else:
        form = ContactFormForm()
    # The line `return render(request, 'contacto.html', {'form': form})` is rendering the
    # 'contacto.html' template with a form object passed as context data. This is typically used in
    # Django views to render an HTML template with specific data (in this case, the form object) that
    # can be displayed on the webpage. The form object is being passed to the template under the key
    # 'form', which allows the template to access and display the form fields or data.
    return render(request, 'contacto.html', {'form': form})



