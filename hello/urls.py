from django.conf.urls import url
from .views import say_hello, current_time, offset_time

urlpatterns = [
    url(r'^$', say_hello, name='say_hello'),
    url(r'^time$', current_time, name='current_time'),
    url(r'^other_time/(\d{1,2})$', offset_time, name='offset_time')
]