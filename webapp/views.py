# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader

from api.models import Symptom


def render_webapp(requests):
    template = loader.get_template('webapp/index.html')
    context = {
        'symptom': Symptom.objects.all()
    }
    return HttpResponse(template.render(context))
