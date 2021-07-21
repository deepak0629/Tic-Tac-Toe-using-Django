from django.contrib import admin
from django.urls import path
from player.views import home
from django.contrib.auth.views import LogoutView,LoginView
from django.conf.urls import url
from player.views import new_invitation,accept_invitation
urlpatterns = [
    url(r'home/', home,name="player_home"),
    url(r'login$',LoginView.as_view(template_name="player/login_form.html"),name="player_login"),
    url(r'logout$',LogoutView.as_view(),name="player_logout"),
    url(r'new_invitaion',new_invitation,name='player_new_invitation'),
    url(r'accept_invitation/(?P<id>\d+)/$',accept_invitation,name="player_accept_invitation")

]