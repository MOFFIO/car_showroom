from functools import wraps
from django.shortcuts import render

def render_to_template(template):
    def inner_render(view):
        def wrapped(request, *args, **kwargs):
            return render(request, template, view(request, *args, **kwargs))
        return wraps(view)(wrapped)
    return inner_render
