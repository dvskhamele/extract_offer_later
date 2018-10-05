from django.conf.urls import include, url
from django.contrib import admin
from dash import views
from django.conf.urls.i18n import i18n_patterns
from dash.views import *

from rest_framework import routers
from django.conf.urls import include, url

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^config/', admin.site.urls),
    url(r'^', include('dash.urls', namespace="dash")),
]
