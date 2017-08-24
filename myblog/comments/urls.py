# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/article/(?P<article_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
    url(r'^search/$', views.search, name='search'),
]