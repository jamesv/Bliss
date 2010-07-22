#####
# Title: bliss.urls.py
#
# Controls the direction of various URLs within the site
#
#
from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns  = patterns('')

urlpatterns += patterns('',
    (r'^img/(?P<path>.*)$',  'django.views.static.serve',
                                    {'document_root': settings.MEDIA_IMG_ROOT}),
    (r'^js/(?P<path>.*)$',  'django.views.static.serve',
                                    {'document_root': settings.MEDIA_JS_ROOT}),
    (r'^css/(?P<path>.*)$',  'django.views.static.serve',
                                    {'document_root': settings.MEDIA_CSS_ROOT}),

    (r'^media/(?P<path>.*)$',  'django.views.static.serve',
                                    {'document_root': settings.ADMIN_MEDIA_ROOT}),

    (r'^$',                         'bliss.wedding.views.home'),
    (r'^wedding/',                  include('bliss.wedding.urls')),
)
