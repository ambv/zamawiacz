from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^zamawiacz/', include('zamawiacz.foo.urls')),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/admin/'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^drukuj-na-jutro/$', 'zamawiacz.zamawianie.views.print_tomorrow'),
)
