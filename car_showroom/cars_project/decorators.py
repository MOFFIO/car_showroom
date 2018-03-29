from django.template import RequestContext
from functools import wraps
from django.shortcuts import render_to_response

def render_to_template(template):
    def inner_render(view):
        def wrapped(request, *args, **kwargs):
            return render_to_response(template, view(request, *args, **kwargs), request)
        return wraps(view)(wrapped)
    return inner_render


