import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Group ,Messages
from channels.db import database_sync_to_async
from django.core.exceptions import PermissionDenied

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        user_permission=await self.check_user_permission(self.room_name)

        if not user_permission:
            raise PermissionDenied
        else:
            pass
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user=self.scope['user']
        group_id=self.room_name
        message=await self.create_message(user,message,group_id)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message.message,
            }
        )

    @database_sync_to_async
    def create_message(self, user,message ,group_id):
        group=Group.objects.get(id=group_id)
        message=Messages.objects.create(sender=user, group=group , message=message)
        return message

    @database_sync_to_async
    def check_user_permission(self,group_id):
        return self.scope['user'].users.filter(id=group_id).exists()



    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))