# -*- coding: utf-8 -*-
from functools import wraps
from django.shortcuts import render

def render_to_template(template):
    def inner_render(view):
        def wrapped(request, *args, **kwargs):
            return render(request, template, view(request, *args, **kwargs))
        return wraps(view)(wrapped)
    return inner_render


def add_var(function_to_decorate):
    def the_wrapper(*args, **kwargs):
        kwargs['extra'] = 11
        result = function_to_decorate(*args, **kwargs)
        return result
    return the_wrapper
