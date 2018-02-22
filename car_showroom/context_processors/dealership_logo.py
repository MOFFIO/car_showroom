# -*- coding: utf-8 -*-

def dealer_logo(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        dealer = request.user.org
        d_logo = dealer.logo
        return {"d_logo":d_logo}
    return {}

