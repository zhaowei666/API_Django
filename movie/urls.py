from django.conf.urls import url
from views import quotes

urlpatterns = [
    url(r'^quotes$', quotes, name="quotes")
]