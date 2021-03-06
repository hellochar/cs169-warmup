from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warmup.views.home', name='home'),
    # url(r'^warmup/', include('warmup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'loginapp.views.homepage'),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'homepage.html'}),
    url(r'^users/login$', 'loginapp.views.login'),
    url(r'^users/add$', 'loginapp.views.add'),
    url(r'^TESTAPI/resetFixture$', 'loginapp.views.resetFixture'),
    url(r'^TESTAPI/unitTests$', 'loginapp.views.unitTests'),
)

urlpatterns += staticfiles_urlpatterns()

