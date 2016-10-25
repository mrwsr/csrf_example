from django.conf.urls import url

import csrf_attack.views


urlpatterns = [
    url(r'^totallyharmless/', csrf_attack.views.evil_csrf),
    url(r'^actuallyharmless/', csrf_attack.views.defeated_csrf),
]
