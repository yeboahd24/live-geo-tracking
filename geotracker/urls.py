# geotracker/urls.py

from django.contrib import admin
from django.urls import path
from tracker.views import track_user_location, show_map

urlpatterns = [
    path('admin/', admin.site.urls),
    path('track-user-location/', track_user_location, name='track-user-location'),
    path('map/', show_map, name='show-map')
]