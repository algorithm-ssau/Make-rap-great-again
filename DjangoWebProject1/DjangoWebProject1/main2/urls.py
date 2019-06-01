from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    #url(r'^$', views.home, name='home'),
    url(r'^$', views.home2, name='home2'),
    url(r'^find_punches', views.punch, name='punch'),
    url(r'^(?P<seasons_id>\w+)/$', views.season1, name='season1'), 
]
