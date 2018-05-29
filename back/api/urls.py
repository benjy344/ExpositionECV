from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artworks/$', views.getallartworks, name='get all artworks'),
    url(r'^artworks/search$', views.getallartworkbyparams, name='search for an artworks from parameters'),
    url(r'^artworks/(?P<pk>[0-9]+)/$', views.getartwork, name='search for an artworks from id'),
    url(r'^artworks/(?P<pk>[0-9]+)/addlike$', views.addlike, name='add a like on artwork with a token'),
    url(r'^artworks/(?P<pk>[0-9]+)/removelike', views.removelike, name='same as like but remove'),
    url(r'^artworks/(?P<pk>[0-9]+)/likes', views.getlikesbyartwork, name='get all the like of an artwork'),
    url(r'^places/$', views.getallplaces, name='get all places'),
    url(r'^places/(?P<pk>[0-9]+)/$', views.getplace, name='get a place from an id'),
    url(r'^places/(?P<pk>[0-9]+)/map/$', views.getplacemap, name='get the map of the place'),
    url(r'^places/(?P<pk>[0-9]+)/rooms/$', views.getallroomsbyplace, name='get all rooms of a place with an id'),
    url(r'^rooms/(?P<pk>[0-9]+)/$', views.getroom, name='get a room from an id'),
    url(r'^rooms/(?P<pk>[0-9]+)/artworks/$', views.getartworkbyroom, name='get all artworks by rooms with an id'),
    url(r'^places/(?P<pk>[0-9]+)/pages/$', views.getpageplace, name='get content for a place by his id'),
    url(r'^places/(?P<pk>[0-9]+)/pages/info$', views.getpageplaceinfos, name='get the content ofinfo for a place'),
    url(r'^places/(?P<pk>[0-9]+)/pages/home$', views.getpageplacehome, name='get the content of home for a place'),
    url(r'^likes/token/$', views.getlikesbytoken, name='Get all likes for a token'),
]


