from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', app.views.home, name='home'),
    url(r'^$', views.home, name='home')
]
