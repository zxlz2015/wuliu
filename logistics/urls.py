from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('books.urls')),
    url(r'^chats/', include('chats.urls')),
    url(r'^maps/', include('maps.urls')),
)

urlpatterns += patterns(
    'logistics.views',
    url(r'^$', 'index'),
    url(r'^index/$', 'index'),
    # url(r'^map/$', 'map'),
    # url(r'^list/$', 'list'),
    # url(r'^orderList/$', 'orderList'),
    url(r'^message/$', 'message'),
    # url(r'^log/$', 'log'),
    # url(r'^test/$', 'test'),
    # url(r'^home/$', 'home'),
)


urlpatterns += patterns(
    '',
    (r'^foo/$', 'logistics.views.foobar_view', {'template_name': 'template1.html'}),
    (r'^bar/$', 'logistics.views.foobar_view', {'template_name': 'template2.html'}),
)
