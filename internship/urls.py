# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'landingpage.views.home'),
    url(r'^8b/', 'landingpage.views.huit'),
    url(r'^admin/', include(admin.site.urls)),
)
