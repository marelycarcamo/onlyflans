# The code snippet is importing necessary modules and views for setting up URL patterns in a Django
# web application. Here's what each import statement does:
from django.contrib import admin
from django.urls import include, path
from web import views


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", views.index, name="index"),
    path("acerca/", views.about, name="about"),
    path("bienvenido/", views.welcome, name="welcome"),
    path("contacto/", views.contacto, name="contacto"),
    path("exito/", views.contacto_success, name="contacto_success"),

  

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/", views.login, name="login"),
    
    path("accounts/logout/", views.logout, name="logout"),
    path("cafeteria/", views.coffee, name="coffee"),
    path("delicias/", views.delicias, name="delicias"),
    path('empresa/',views.contacto_empresa, name='contacto_empresa'),

    path("facebook/", views.facebook_redirect, name="facebook_redirect"),
    path("twitter/", views.twitter_redirect, name="twitter_redirect"),
    path("instagram/", views.instagram_redirect, name="instagram_redirect"),
    path("empresa/", views.contacto_empresa, name="contacto_empresa"),

    
]

