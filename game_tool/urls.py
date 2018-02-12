from django.conf.urls import url
from .views import create_room, draw_character

urlpatterns = [
    url(r'^create_room$', create_room, name='create_room'),
    url(r'^draw_character$', draw_character, name='draw_character')
]