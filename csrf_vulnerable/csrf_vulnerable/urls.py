from django.conf.urls import url

import csrf_vulnerable.views


urlpatterns = [
    url(r'^transfer/', csrf_vulnerable.views.transfer),
]
