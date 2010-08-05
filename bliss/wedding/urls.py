#####
# Title: bliss.wedding.urls.py
#
# Controls the direction of various URLs within the site
#
#

from django.conf.urls.defaults import *
urlpatterns  = patterns('')

###
# Title: Wedding routing
#
# routing for end user views
#

urlpatterns += patterns('bliss.wedding.views',
    url(r'^$','home',name='wedding-home'),
    url(r'^about/$','about',name='wedding-about'),
    url(r'^day/(?P<id>[1-4]{1})/$','day',name='wedding-day'),
    
        
)