# Create your views here.
from django.shortcuts import render

from projects.manage.status_code.mongodb.mongodb_status_code_processor import MongoDBStatusCodeProcessor
from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)


def process_status_code(request):
    path = "full_path"
    status_code_response = MongoDBStatusCodeProcessor().process_status_code(full_file_path=path)
    context = {"projects": status_code_response}
    return render(request, "project_index.html", context)