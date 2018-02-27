"""Models for the api."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Symptom(models.Model):
    """Symptom connected to a Condition."""
    name = models.CharField(max_length=32)
    # How many times the symptom has been searched on the API.
    search_count = models.IntegerField(default=0)


class Condition(models.Model):
    """Medical condition."""
    name = models.CharField(max_length=32)
    symptoms = models.ManyToManyField(Symptom, related_name='conditions')
