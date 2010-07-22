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
    ['day_2',   'day 2',    0],
    ['day_3',   'day 3',    0],
    ['day_4',   'day 4',    0],
    ['day_5',   'day 5',    0],
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
    

