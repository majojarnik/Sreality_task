from django.shortcuts import render
from .models import Flat


def index(request):
    flats_list = Flat.objects.all()
    context = {"flats_list": flats_list}
    return render(request, "flats/index.html", context)
