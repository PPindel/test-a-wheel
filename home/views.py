from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to render index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to render contact page """

    return render(request, 'home/contact.html')
