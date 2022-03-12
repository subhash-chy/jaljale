from django.shortcuts import get_object_or_404, render

from home.models import Banner
from setting.models import SiteSetting
from .models import Project


def ongoing_projects(request):
    logo = Banner.objects.last()
    site_setting = SiteSetting.objects.last()
    ongoing_projects = Project.objects.filter(status='Ongoing')

    context = {
        'logo': logo,
        'siteSettings': site_setting,
        'projects': ongoing_projects,
        }
    return render(request, 'project/projects.html', context)


def completed_projects(request):
    logo = Banner.objects.last()
    site_setting = SiteSetting.objects.last()
    completed_projects = Project.objects.filter(status='Completed')

    context = {
        'logo': logo,
        'siteSettings': site_setting,
        'projects': completed_projects,
        }
    return render(request, 'project/projects.html', context)


def view_project(request, id=None):
    site_setting = SiteSetting.objects.last()
    project = get_object_or_404(Project, pk=id)
    context = {
        'siteSettings': site_setting,
        'project': project,
        }
    return render(request, 'project/project_detail.html', context)