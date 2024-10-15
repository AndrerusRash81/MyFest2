import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import main.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybase.settings')

application = ProtocolTypeRouter({
   "http": get_asgi_application(),
   "websocket": URLRouter(main.routing.websocket_urlpatterns),
})

