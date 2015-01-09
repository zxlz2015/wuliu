# coding=utf-8

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'books.views',
    url(r'^contact/$', 'contact'),
    url(r'^contact/thanks$', 'contact_thanks'),
)