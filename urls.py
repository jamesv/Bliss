from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import bliss.urls


urlpatterns = patterns('',
    (r'^tools/', include(admin.site.urls)),
)

urlpatterns += bliss.urls.urlpatterns