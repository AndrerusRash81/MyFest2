import os
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
#from ..main import routing
from main import routing
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybase.settings')

django.setup()

application = ProtocolTypeRouter({
   "http": get_asgi_application(),
   #"websocket": URLRouter(routing.websocket_urlpatterns),
   "websocket": AuthMiddlewareStack(
      URLRouter(routing.websocket_urlpatterns)
   ),
})

