# Encoding: utf-8

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from ddlseite.models import *

def index(request):
    projects = Project.objects.filter(listinindex=True).order_by('name')
    def Filesizes():
      x = Episode.objects.all()
      Allfiles = 0
      for files in x:
	Allfiles += files.filesize
      return Allfiles/1000
    Filenum = Episode.objects.count()
    return render_to_response('ddlseite/index.html',locals())

def projectview(request, project_id):
    proj_descr = get_object_or_404(Project, pk=project_id)
    proj_state = Status.objects.filter(project__exact=project_id)
    who_did = Who_did_what.objects.filter(project__exact=project_id)
    dls = Episode.objects.filter(project__exact=project_id).order_by('number')
    tabellentitel = table_title.objects.filter(project__exact=project_id)
    return render_to_response('ddlseite/project.html', locals())

# EOF views.py
