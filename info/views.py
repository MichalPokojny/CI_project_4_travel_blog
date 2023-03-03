from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "index.html"


class Contact(TemplateView):
    template_name = "contact.html"


class About(TemplateView):
    template_name = "about.html"