from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "client/index.html")


def menu(request):
    return render(request, "client/menu.html")


def gallery(request):
    return render(request, "client/gallery.html")


def registration(request):
    return render(request, "client/registration.html")


def about(request):
    return render(request, "client/about.html")


def contact(request):
    return render(request, "client/contact.html")
