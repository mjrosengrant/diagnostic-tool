from django.conf.urls import url

import api.views as views

urlpatterns = [
    url(r'symptoms/$', views.list_symptoms, name='symptoms-list'),
    url(r'symptoms/(?P<symptom_pk>[0-9])/$', views.get_conditions_for_symptom, name='symptom-conditions'),
]
