import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, Page
from pagination.settings import BUS_STATION_CSV

DATA = []
with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
    stations_list = csv.DictReader(csvfile)
    for item in stations_list:
        DATA.append(item)

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(DATA, 10)
    comtent = paginator.get_page(current_page)
    page = Page(DATA, current_page, paginator)

    context = {
        'bus_stations': comtent,
        'page': page,
    }
    return render(request, 'stations/index.html', context)