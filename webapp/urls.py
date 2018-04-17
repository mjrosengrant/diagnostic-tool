from django.conf.urls import url

import webapp.views as views

urlpatterns = [
    url(r'$', views.render_webapp, name='webapp'),
]
