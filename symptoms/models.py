"""Models for the symptoms app."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Symptom(models.Model):
    """Symptom connected to a Condition."""
    name = models.CharField(max_length=32)


class Condition(models.Model):
    """Medical condition."""
    name = models.CharField(max_length=32)
    symptoms = models.ManyToManyField(Symptom, related_name='conditions')
