from django.contrib import admin

import mrmgr.rackit.models


admin.site.register(mrmgr.rackit.models.Rack)
admin.site.register(mrmgr.rackit.models.Platform)
admin.site.register(mrmgr.rackit.models.Machine)
