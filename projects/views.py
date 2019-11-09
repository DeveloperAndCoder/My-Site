from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    truncate_at = 50
    for project in projects:
        project.description = (project.description[:truncate_at] + '...') if len(project.description) > truncate_at else project.description
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
