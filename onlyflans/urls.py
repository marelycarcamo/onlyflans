

# The code snippet is importing necessary modules and views for setting up URL patterns in a Django
# web application. Here's what each import statement does:
from django.contrib import admin
from django.urls import include, path
from web import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),    
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.contacto_success, name='contacto_success'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('accounts/login/', views.login, name='login'),

        # path('login_welcome/', views.login_welcome, name='login_welcome'),
    # path('accounts/logout/', views.logout, name='logout'),

]