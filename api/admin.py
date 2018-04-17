# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import Condition, Symptom

admin.site.register(Condition)
admin.site.register(Symptom)
