#####
# Title: bliss.templatetags.ui.py
#
# Draws UI snippets
#
#

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django import template
from django.conf import settings


register = template.Library()

NAV_ITEMS = [
    ['home',    'main',     ''],
    ['about',   'about',    'about/'],
    ['day_1',   'day 1',    'day/1/'],
    ['day_2',   'day 2',    'day/2/'],
    ['day_3',   'day 3',    'day/3/'],
    ['day_4',   'day 4',    'day/4/'],
    ['day_5',   'day 5',    'day/5/'],
]

@register.filter()
def drawNav(value):
    nav  = "<ul id='nav'>"
    for nav_item in NAV_ITEMS:
        nav += "	<li id='nav_"+nav_item[0]+"'>"
        
        #Is a link?
        if nav_item[2] != 0:
            
            #Is the current page?
            if value == nav_item[0]:
                css_class = 'current'
            else:
                css_class = ''
            nav += "<a href='/wedding/"+nav_item[2]+"' class='"+css_class+"'>"+nav_item[1]+"</a>"
        else:
            nav += nav_item[1]
        
        nav += "</li>"
        
        
    nav += "</ul>"
    return mark_safe(nav)
    
@register.filter()
def drawPhotos(photos, prefix=''):
    gallery  = "<div class='glowBox g photos'>"
    gallery += "<div id='"+prefix+"slideshow' class='slideshow'></div>"
    gallery += "<div id='"+prefix+"thumbs' class='ac'>"
    gallery += "	<ul class='thumbs noscript'>"
    for photo in photos:
        gallery += "		<li>"
        gallery += "			<a class='thumb' href='/img/photos/"+photo[0]+".jpg' title='"+photo[1]+"'>"
        gallery += "				<img src='/img/photos/"+photo[0]+"_t.jpg' alt='"+photo[1]+"' />"
        gallery += "			</a>"
        gallery += "		</li>"
    gallery += "	</ul>"
    gallery += "</div>"
    gallery += "<div id='"+prefix+"controls' class='controls'></div>"
    gallery += "<script>"
    gallery += "jQuery(document).ready(function($) {"
    gallery += "    var gallery = $('#"+prefix+"thumbs').galleriffic({"
    gallery += "        delay:                     3000, "
    gallery += "        imageContainerSel:         '#"+prefix+"slideshow', "
    gallery += "        controlsContainerSel:      '#"+prefix+"controls', "
    gallery += "    });"
    gallery += "});"
    gallery += "</script>"
    gallery += "</div>"
    
    return mark_safe(gallery)
    
    
    
    
    

