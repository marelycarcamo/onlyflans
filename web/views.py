from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# def index(request):
#   return render(request, 'index.html')

# def about(request):
#   return render(request, 'about.html')

# def welcome(request):
#   return render(request, 'welcome.html')



from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from web.forms import ContactFormForm

from .models import Cafe, ContactForm, Dulce, Flan




def coffee(request):
    cafes = Cafe.objects.all()  # Filtrar los flanes públicos
    context = {'cafes': cafes}  # Crear un diccionario de contexto con los flanes públicos
    return render(request, 'coffee.html', context)  # Pasar el contexto a la plantilla



def index(request):
    flanes_publicos = Flan.objects.filter(js_private=False)  # Filtrar los flanes públicos
    context = {'flanes': flanes_publicos}  # Crear un diccionario de contexto con los flanes públicos
    return render(request, 'index.html', context)  # Pasar el contexto a la plantilla

def delicias(request):
    dulces = Dulce.objects.all() # Filtrar los flanes públicos
    context = {'dulces': dulces}  # Crear un diccionario de contexto con los flanes públicos
    return render(request, 'delicias.html', context)  # Pasar el contexto a la plantilla


#La vista protegida debe llevar el decorador @login_required
@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(js_private=True)  # Filtrar los flanes públicos
    context = {'flanes': flanes_privados}  # Crear un diccionario de contexto con los flanes públicos
    return render(request, 'welcome.html', context)  # Pasar el contexto a la plantilla


def about(request):
    return render(request, 'about.html')


def base(request):
    return render(request, 'base.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # guardar los datos del formulario en la base de datos
            ContactForm.objects.create(
                customer_email=form.cleaned_data['customer_email'],
                customer_name=form.cleaned_data['customer_name'],
                message=form.cleaned_data['message']
            )
            # Redirigir a una página de éxito
            return redirect ('contacto_success')
            
            # return HttpResponseRedirect('/')
    else:
        form = ContactFormForm()
    # The line `return render(request, 'contacto.html', {'form': form})` is rendering the
    # 'contacto.html' template with a form object passed as context data. This is typically used in
    # Django views to render an HTML template with specific data (in this case, the form object) that
    # can be displayed on the webpage. The form object is being passed to the template under the key
    # 'form', which allows the template to access and display the form fields or data.
    return render(request, 'contacto.html', {'form': form})


def contacto_success(request):
    return render(request, '/contacto_success.html', {'success': True})


def login(request):
    return redirect ('/accounts/login.html')

# def logout(request):
#     return redirect ('/accounts/logout.html')

def  logout(request):
    return render(request, 'logout.html', {'message': '¡Hasta pronto! Vuelve pronto.'})



def facebook_redirect(request):
    return redirect('https://web.facebook.com/Cafe.Cosas.Ricas.Valdivia/?_rdc=1&_rdr')

def twitter_redirect(request):
    return redirect('https://twitter.com/cafecosasricas')

def instagram_redirect(request):
    return redirect('https://www.instagram.com/cosasricas.valdivia/')


def logo_onlyflans_redirect(request):
    return redirect('https://photos.onedrive.com/share/22F87BD4A80CE19A!327001?cid=22F87BD4A80CE19A&resId=22F87BD4A80CE19A!327001&authkey=!ABHVndQy7jl0pDk&ithint=photo&e=aVkvph')
            