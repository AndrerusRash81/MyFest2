import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

#получение времени
from datetime import date, datetime

class ChatConsumer(AsyncWebsocketConsumer):
 async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        #print("====new chat=====")
        #print(self.channel_name)
        #print(self.scope['user'])

        await self.accept()

 async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

 async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        event = text_data_json.get("event", None)

        #print("====receive chat=====")
        #print(event)
        #print(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'my_chat_message',
                'message': message
            }
        )

 async def my_chat_message(self, event):
        message = event['message']
        print("====chat_message chat=====")
        print(message)
        #Время попробуем посылать совместно с сообщениями
        today = date.today()
        # Формат dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        # Объект datetime, содержащий текущую дату и время
        now = datetime.now()
        # Формат dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        message=d1+"-"+dt_string+"-"+message

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

class ChatConsumer_sinxron(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))