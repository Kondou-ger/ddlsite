# Encoding: utf-8
from ddlseite.models import *
from django.contrib import admin

class AufgabeInline(admin.TabularInline):
    model = Who_did_what
    extra = 1
    
class DLInline(admin.TabularInline):
    model = Episode
    extra = 1
    
class TbtitleInline(admin.TabularInline):
    model = table_title
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Projektname',          {'fields': ['name']}),
        ('Fortschritt',          {'fields': ['progress']}),
        ('Status',               {'fields': ['state']}),
        ('Beschreibung & Stuff', {'fields': ['image','genre','number_of_episodes','torrentbatch','listinindex'], 'classes': ['collapse']})
    ]
    inlines = [AufgabeInline, TbtitleInline, DLInline]
    list_display = ('name', 'progress', 'state','listinindex',)
    list_filter = ('state','listinindex',)
    search_fields = ['name']    
    
class StatusAdmin(admin.ModelAdmin):
    list_display = ('stat', 'hexcol',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Nick)
admin.site.register(Genrecollect)
admin.site.register(Taskcollect)
admin.site.register(Status, StatusAdmin)

# EOF admin.py