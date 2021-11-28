from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.

#main page
class Main(TemplateView):
    template_name = "main.html"
