from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes noms sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def about(request):

    return HttpResponse("<h1>À propos de nous:<h1> <p> WassolonShop votre boutique. Nous existons que pour vous servir</p>")

