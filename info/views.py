from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


class Home(TemplateView):
    template_name = "index.html"


class Contact(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['API_KEY'] = settings.EMAIL_API_KEY
        return context


class About(TemplateView):
    template_name = "about.html"