# coding=utf-8

from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'maps.views',
    url(r'^$', 'index'),
    url(r'^map/$', 'index'),
    url(r'^list/$', 'list'),
    url(r'^orderList/$', 'orderList'),
    url(r'^message/$', 'message'),
    url(r'^log/$', 'log'),
    url(r'^test/$', 'test'),
    url(r'^home/$', 'home'),
    url(r'^error/$', 'error'),
    url(r'^log_list/$', 'log_list'),
    url(r'^login/$', 'login'),
    url(r'^register/$', 'register'),
    url(r'^json/$', 'json'),
)
