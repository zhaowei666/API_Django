from django.conf.urls import url
from .views import post_lists, register

urlpatterns = [
    url(r'^posts$', post_lists, name='post_lists'),
    url(r'^register$', register, name='register')
]

