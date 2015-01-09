# coding=utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'chats.views',
    (r'^$', 'chats'),
)
