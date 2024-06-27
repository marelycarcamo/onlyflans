

# The code snippet is importing necessary modules and views for setting up URL patterns in a Django
# web application. Here's what each import statement does:
from django.contrib import admin
from django.urls import path
from web import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),    
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.contacto_success, name='contacto_success'),
    
]
