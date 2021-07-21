from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from gameplay.views import game_detail
urlpatterns = [
    url(r'detail/(?P<id>\d+)/$',game_detail,name='gameplay_detail')
    ]