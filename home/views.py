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


def error_403_view(request, exception):
    """
    Displays 403.html path
    """

    return render(request, 'errors/403.html')


def error_404_view(request, exception):
    """
    Displays 404.html path
    """

    return render(request, 'errors/404.html')


def handler500(request, *args, **argv):
    """
    Displays 500.html path
    """
    return render(request, 'errors/500.html')
