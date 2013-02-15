
from django.conf.urls import patterns, include, url

urlpatterns = patterns('users',
    url(r'^login/$', 'login'),
    url(r'^add/$', 'detail'),
)

