#Encoding: utf-8
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', include('ddlseite.urls')), #temp, braucht ne richtige Index-Seite
    (r'^ddl/', include('ddlseite.urls'))
)
