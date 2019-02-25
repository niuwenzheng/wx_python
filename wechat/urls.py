from django.urls import path,include
from werobot.contrib.django import make_view
from .robot import myrobot

urlpatterns = [
    path('', make_view(myrobot)),
]