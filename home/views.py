# Import necessary module for rendering views
from django.shortcuts import render


# View to render the index page
def index(request):
    """ A view to render index page """
    return render(request, 'home/index.html')


# View to render the contact page
def contact(request):
    """ A view to render contact page """
    return render(request, 'home/contact.html')


# View to render the FAQ page
def faq(request):
    """ A view to render faq page """
    return render(request, 'home/faq.html')
