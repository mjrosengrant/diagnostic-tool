from django.conf.urls import url

import views

urlpatterns = [
    url(r'$', views.render_webapp, name='webapp'),
]
