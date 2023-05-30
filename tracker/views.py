
from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mapbox import Geocoder
from tracker.models import UserLocation

geocoder = Geocoder(access_token='pk.eyJ1IjoiZG9taW5pYzcwIiwiYSI6ImNrcTIxZjBndjBrZ3UydXA4Y3MwczZyZDIifQ.SkvFr88vsy5lchvgoJAkEA')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
def track_user_location(request):
    ip_address = get_client_ip(request)
    data = geocoder.forward(ip_address).json()
    latitude = data['features'][0]['center'][1]
    longitude = data['features'][0]['center'][0]
    print(latitude, longitude)

    user_location = UserLocation(
        ip_address=ip_address,
        latitude=latitude,
        longitude=longitude,
    )
    user_location.save()

    response = {
        'latitude': latitude,
        'longitude': longitude,
    }
    return JsonResponse(response)

def show_map(request):
    return render(request, 'map.html')