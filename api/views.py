# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Symptom


def list_symptoms(requests):
    """Print list of all symptoms available in database."""
    data = {
        "results": [
            {
                "name": symptom.name,
                "pk": symptom.pk
            } for symptom in Symptom.objects.all()
        ]
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_conditions_for_symptom(requests, symptom_pk):
    """Print conditions associated with provided symptom."""
    symptom = get_object_or_404(Symptom, pk=symptom_pk)
    symptom.search_count += 1
    symptom.save()

    data = {
        "results": [
            {
                "name": condition.name,
                "pk": condition.pk
            } for condition in symptom.conditions.all()
        ]
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
