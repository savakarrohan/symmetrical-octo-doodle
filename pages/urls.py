from django.urls import path 
# Importing the views
from .views import HomePageView
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
