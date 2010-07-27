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
    data['photos'] = [
        ['00_00_couple', 'fpo'],
    ]
    template = "wedding/day_1.html"

    return render_to_response(template, data)