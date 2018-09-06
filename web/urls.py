# -*- coding: utf-8 -*-

from django.conf.urls import url
from web.views import index

urlpatterns = [
    url(r'^$', index.index, name="index"),
]