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
    data = {}
    template = "wedding/home.html"
    
    return render_to_response(template, data)