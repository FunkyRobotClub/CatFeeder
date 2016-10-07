from django.shortcuts import render
from django.http import HttpResponse
from .Feeder.src.DataLogger import get_data


def data(request):
    return render(request, "interface/data.html", {"data": [get_data()]})
    # return HttpResponse("<p>Stuff</p>")
