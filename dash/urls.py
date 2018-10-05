# -*- coding: utf-8 -*
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.challan, name='challan'),
    url(r'review/^$', views.review, name='review'),
]