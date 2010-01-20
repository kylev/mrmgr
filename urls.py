from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^mrmgr/', include('mrmgr.rackit.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_ROOT}),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
