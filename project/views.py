from django.shortcuts import render

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
        'ongoing_projects': ongoing_projects,
        }
    return render(request, 'project/projects.html', context)


def completed_projects(request):
    logo = Banner.objects.last()
    site_setting = SiteSetting.objects.last()
    completed_projects = Project.objects.filter(status='Ongoing')

    context = {
        'logo': logo,
        'siteSettings': site_setting,
        'completed_projects': completed_projects,
        }
    return render(request, 'project/projects.html', context)
