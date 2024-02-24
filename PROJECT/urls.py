from django.contrib import admin
from django.urls import path
from chat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', index, name='index'),
    path('chat/<str:room_name>/', room, name='room'),
]
