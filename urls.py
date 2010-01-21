from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Do included URLs later?
    #(r'^mrmgr/', include('mrmgr.rackit.urls')),
    # Main application URLs
    (r'^$', 'mrmgr.rackit.views.index'),
    (r'^rack/(?P<rack_id>\w+)/$', 'mrmgr.rackit.views.showrack'),
    (r'^rack_order/(?P<rack_id>\w+)/$', 'mrmgr.rackit.views.save_order'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_ROOT}),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
