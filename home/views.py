# Import necessary module for rendering views
from django.shortcuts import render


def index(request):
    """ A view to render index page """
    return render(request, 'home/index.html')


def contact(request):
    """ A view to render contact page """
    return render(request, 'home/contact.html')


def faq(request):
    """ A view to render faq page """
    return render(request, 'home/faq.html')
