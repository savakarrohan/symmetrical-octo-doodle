from django.urls import path 
# Importing the views
from .views import HomePageView, AboutPageView
urlpatterns = [
    path("about/",AboutPageView.as_view(),name='about'),
    path("", HomePageView.as_view(), name="home"),
]
