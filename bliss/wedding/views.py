#####
# Title: bliss.wedding.views.py
#
# Display views for marriage based activities
#
#

from django.shortcuts import render_to_response


###
# Function: home
#
# Wedding home/intro view
#
# Parameters:
#
# Returns:
#   *render_to_response*
#
def home(request):
    data = {'curr_page':'home'}
    data['photos'] = [
        ['00_00_couple', 'fpo'],
        ['00_00_couple', 'fpo'],
        ['00_00_couple', 'fpo'],
    ]
    template = "wedding/home.html"
    
    return render_to_response(template, data)
    
###
# Function: about
#
# About Us view
#
# Parameters:
#
# Returns:
#   *render_to_response*
#
def about(request):
    data = {'curr_page':'about'}
    data['photos'] = [
        ['00_00_couple', 'Smile'],
        ['00_01_wonderland', 'Wonderland NYE 2009'],
        ['00_02_strawberry', 'We found a carnival graveyard in the woods'],
        ['00_03_petes', 'Just being domestic and walking the dog'],
        ['00_04_lady_glasses', 'James looks good in lady glasses'],
        ['00_05_fireside', 'Our first trip to the Peppermill Lounge'],
        ['00_06_fish', 'Sleeping with artists'],
        
    ]
    template = "wedding/about.html"

    return render_to_response(template, data)
    
###
# Function: day
#
# Displays a given day's overview
#
# Parameters:
#
# Returns:
#   *render_to_response*
#
def day(request, id):
    data = {'curr_page':'day_'+id}
    
    if id == '1':
        data['photos'] = [
            ['01_01_graceland', ''],
            ['01_02_graceland_smooch', ''],
            ['01_03_simmons_graceland', ''],
            ['01_04_scary_driving', ''],
            ['01_05_hot_wife', ''],
            ['01_06_glitter', ''],
            ['01_07_lf8r', ''],
            ['01_08_dtw', ''],
            ['01_09_license', ''],
            ['01_10_bureau', ''],
            ['01_11_hallway', ''],
        ]
    elif id == '2':    
        data['photos'] = [
            ['02_01_stripper', ''],
            ['02_02_ant', ''],
            ['02_03_pool_james', ''],
            ['02_04_pool_amanda', ''],
            ['02_05_buffet', ''],
            ['02_06_nap', ''],
            ['02_07_cowgirl', ''],
            ['02_08_freemont', ''],
        ]
    template = "wedding/day_"+id+".html"

    return render_to_response(template, data)