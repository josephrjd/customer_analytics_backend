from django.conf.urls import url
from .views import First


urlpatterns = [
    url(r'^', First.as_view(), name='application'),
]