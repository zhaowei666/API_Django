from django.conf.urls import url
from .views import post_lists

urlpatterns = [
    url(r'^$', post_lists, name='post_lists')
]

