# Encoding: utf-8
from django.conf.urls.defaults import *

urlpatterns = patterns('ddlseite.views',  # 
    (r'^$','index'),
    (r'^index/$','index'),
    (r'(?P<project_id>\d+)/$', 'projectview')
)

# EOF ddlseite.urls.py