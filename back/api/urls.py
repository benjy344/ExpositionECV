from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^place/(?P<pk>[0-9]+)/pages/infos$', views.getpageplace, name='getpageplace'),
]
