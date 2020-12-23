from django.shortcuts import render
from .models import Prod

# Create your views here.


def wineproducts(request):

    wines = Prod.objects.all()

    context = {
        'wines': wines,
    }

    return render(request, 'wines/wines.html', context)
