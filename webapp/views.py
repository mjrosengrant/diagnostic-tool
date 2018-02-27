# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

def render_webapp(requests):
    t = loader.get_template('webapp/index.html')
    return HttpResponse(t.render({'api_url': '127.0.0.1:8000/api/symptoms'}))
