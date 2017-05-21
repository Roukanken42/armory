from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^gear/(?P<id>[1-9][0-9]*)/?$', views.gear, name='gear'),
    url(r'^upload/?$', views.upload, name='upload'),
    url(r'^search/?$', views.search, name='search'),
    url(r'^compare/?$', views.compare, name='compare'),
    url(r'^compare/(?P<p1>[1-9][0-9]*)/?$', views.compare, name='compare'),
    url(r'^compare/(?:(?P<p1>[1-9][0-9]*))/(?P<p2>[1-9][0-9]*)/?$', views.compare, name='compare'),
    url(r'^player/(?P<id>[1-9][0-9]*)/?$', views.player, name='player'),
    url(r'^$', views.index, name='index'),
]