from django.conf.urls import url

import csrf_vulnerable.views
import csrf_vulnerable.safe_views


urlpatterns = [
    url(r'^transfer/', csrf_vulnerable.views.transfer),
    url(r'^safetransfer/', csrf_vulnerable.safe_views.transfer),
]
