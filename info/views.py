from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


class Home(TemplateView):
    """
    Class based view for the home page
    """
    template_name = "index.html"


class Contact(TemplateView):
    """
    Class based view for the contact page
    """
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        """
        Adds the emailJS API key from Django settings
        to the context dictionary.
        """
        context = super().get_context_data(**kwargs)
        context['API_KEY'] = settings.EMAIL_API_KEY
        return context


class About(TemplateView):
    """
    Class based view for the Abouts Us page
    """
    template_name = "about.html"
