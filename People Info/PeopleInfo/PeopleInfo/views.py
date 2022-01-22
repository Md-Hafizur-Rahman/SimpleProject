from os import name
from django.shortcuts import render 
from tuition.models import Contact
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mag"] = 'welcome to the website.'
        return context
        