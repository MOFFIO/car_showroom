from django.template.context_processors import request
from django.contrib.auth.decorators import login_required

#from cars_project.models import Dealership

#@login_required(login_url='login/')
def dealer_logo(request):
    if request.user.is_authenticated():
        dealer = request.user.org
        d_logo = dealer.logo
        return {"d_logo":d_logo}
    return {}

