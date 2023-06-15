from django.urls import re_path
from . import views


# Because of the venv, we need to import views from a different folder.

                    
urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^chatter$', views.chatter),
    re_path(r'^send/(?P<text>\w+)$', views.send_text),
]