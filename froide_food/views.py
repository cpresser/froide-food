import json

from django.shortcuts import render, redirect
from django.contrib import messages

from .venue_providers import venue_providers, venue_provider
from .utils import (
    get_hygiene_publicbody, make_request_url, get_city_from_request
)


def index(request):
    city = get_city_from_request(request)
    return render(request, 'froide_food/index.html', {
        'city': json.dumps(city or {}),
        'filters': json.dumps(venue_provider.FILTERS)
    })


def make_request(request):
    ident = request.GET.get('ident')
    if not ident:
        messages.add_message(request, messages.ERROR, 'Fehlerhafter Link')
        return redirect('food-index')
    try:
        provider, ident = ident.split(':')
        if provider not in venue_providers:
            raise ValueError
    except ValueError:
        messages.add_message(request, messages.ERROR, 'Fehlerhafter Link')
        return redirect('food-index')

    place = venue_providers[provider].get_place(ident)
    try:
        pb = get_hygiene_publicbody(place['lat'], place['lng'])
    except ValueError as e:
        messages.add_message(request, messages.ERROR, str(e))
        return redirect('food-index')

    url = make_request_url(place, pb)
    return redirect(url)
