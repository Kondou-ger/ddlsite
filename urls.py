#Encoding: utf-8
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', include('ddlseite.urls')),
    (r'^ddl/', include('ddlseite.urls'))
)
