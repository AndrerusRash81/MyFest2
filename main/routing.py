# Пример routing.py для приложения
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
   # re_path(r'ws/chat_sinxron/(?P<room_name>\w+)/$', consumers.ChatConsumer_sinxron.as_asgi()),
]