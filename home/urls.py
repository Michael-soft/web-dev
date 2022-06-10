from django.urls import path
from .views import home, contact, about

# app urlspattern for the culled from the projects urls 
urlpatterns = [
    path("home/",home),
    path("contact/",contact),
    path("about/",about)   
]
