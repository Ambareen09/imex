from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.index, name="menu"),
    path("gallery", views.index, name="gallery"),
    path("reservation", views.index, name="reservation"),
    path("about", views.index, name="about"),
    path("contact", views.index, name="contact"),
]
