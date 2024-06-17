from django.shortcuts import render

# def index(request):
#   return render(request, 'index.html')

# def about(request):
#   return render(request, 'about.html')

# def welcome(request):
#   return render(request, 'welcome.html')



from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

def welcome(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

def base(request):
    return render(request, 'base.html')
