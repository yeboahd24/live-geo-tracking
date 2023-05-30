from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Location

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        location_data = json.loads(text_data)
        coordinates = location_data['coordinates']
        # Save the location data to the database
        location = Location.objects.create(user=self.scope['user'], coordinates=coordinates)
        # Send an acknowledgment back to the client
        await self.send(json.dumps({'status': 'Location saved.'}))
