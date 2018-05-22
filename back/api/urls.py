from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artwortks/$', views.getallartwortks, name='allartwortks'),
    url(r'^artwortks/search$', views.getallartwortkbyparams, name='allartwortks'),
    url(r'^artwortks/(?P<pk>[0-9]+)/$', views.getartwortk, name='artwortk'),
    url(r'^places/$', views.getallplaces, name='getallplace'),
    url(r'^places/(?P<pk>[0-9]+)/$', views.getplace, name='getplace'),
    url(r'^places/(?P<pk>[0-9]+)/map/$', views.getplacemap, name='getplacemap'),
    url(r'^places/(?P<pk>[0-9]+)/rooms/$', views.getallroomsbyplace, name='getallroomsbyplace'),
    url(r'^rooms/(?P<pk>[0-9]+)/$', views.getroom, name='getroom'),
    url(r'^rooms/(?P<pk>[0-9]+)/artwortks/$', views.getartwortkbyroom, name='getartwortkbyroom'),
    url(r'^places/(?P<pk>[0-9]+)/pages/$', views.getpageplace, name='getpageplace'),
    url(r'^places/(?P<pk>[0-9]+)/pages/info$', views.getpageplaceinfos, name='getpageplaceinfos'),
    url(r'^places/(?P<pk>[0-9]+)/pages/home$', views.getpageplacehome, name='getpageplacehome'),
]


