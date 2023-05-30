from django.urls import re_path
from tracker import consumers

websocket_urlpatterns = [
    re_path(r'ws/locations/$', consumers.LocationConsumer.as_asgi()),
]

