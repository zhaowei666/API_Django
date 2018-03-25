from django.conf.urls import url
from .views import post_lists, register, login_user, logout_user

urlpatterns = [
    url(r'^posts$', post_lists, name='post_lists'),
    url(r'^register$', register, name='register'),
    url(r'^login$', login_user, name='login_user'),
    url(r'^logout', logout_user, name='logout_user')
]

