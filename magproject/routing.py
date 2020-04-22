# from channels.routing import ProtocolTypeRouter , URLRouter
# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
# from django.urls import path
# from django.conf.urls import url

# import magapp.routing


# application = ProtocolTypeRouter({
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 (
#                     magapp.routing.websocket_urlpatterns
#                 )
#             )
#         ),
#     )
# })
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from magapp.consumers import ChatConsumer
import magapp.routing
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            magapp.routing.websocket_urlpatterns
        )
    ),
})
