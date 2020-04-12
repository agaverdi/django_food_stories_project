from django.urls import path,re_path
from .views import room , index



app_name='chatapp'

urlpatterns = [
    # re_path(r"^(?P<username>[\w.@+-]+)",Threadview.as_view()),
    path('index/', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]