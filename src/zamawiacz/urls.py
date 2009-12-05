from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^zamawiacz/', include('zamawiacz.foo.urls')),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/admin/'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
