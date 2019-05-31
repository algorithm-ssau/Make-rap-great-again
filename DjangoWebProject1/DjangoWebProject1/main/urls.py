from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    #url(r'^$', app.views.home, name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^rapper/(?P<rapper_id>\w+)/$', views.rapper1, name='rapper1'), 
]
