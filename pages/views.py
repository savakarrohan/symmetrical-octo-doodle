from django.shortcuts import render
from django.views.generic import TemplateView 
class HomePageView(TemplateView):
    """Currently basic"""
    template_name = "home.html"
