from django.shortcuts import render, redirect
from plant_and_equipment.models import PlatsAndEquipment

from project.models import Project
from service.models import Service

from .models import Banner
from setting.models import SiteSetting
from testimonial.models import Testimonial
from about_us.models import AboutUs
from contact.models import ContactUs


def home(request):
    banners = Banner.objects.all()
    site_setting = SiteSetting.objects.last()
    testimonials = Testimonial.objects.all()
    about_us = AboutUs.objects.last()
    projects = Project.objects.all()[:4]

    context = {
        'siteSettings': site_setting,
        'testimonials': testimonials,
        'aboutUs': about_us,
        'projects': projects,
        'banners': banners,
    }
    return render(request, 'home/index.html', context)


def about_us(request):
    site_setting = SiteSetting.objects.last()
    about_us = AboutUs.objects.last()

    context = {
        'siteSettings': site_setting,
        'aboutUs': about_us,

    }
    return render(request, 'home/about_us.html', context )


def contact_us(request):
    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        messages = request.POST['message']

        ContactUs.objects.create(name=name, email=email, message=messages);
        return redirect("home:index")
        
    else:
        logo = Banner.objects.last()
        site_setting = SiteSetting.objects.last()

        context = {
            'logo': logo,
            'siteSettings': site_setting,
            }
        return render(request,"home/contact_us.html", context)


def services(request):
    site_setting = SiteSetting.objects.last()
    service_col1 = Service.objects.filter(column=1)
    service_col2 = Service.objects.filter(column=2)

    context = {
        'siteSettings': site_setting,
        'service_col1': service_col1,
        'service_col2': service_col2,
        }
    return render(request, 'home/services.html', context)


def plants_equipments(request):
    site_setting = SiteSetting.objects.last()
    plants_equipments = PlatsAndEquipment.objects.all()

    context = {
        'siteSettings': site_setting,
        'plants_equipments': plants_equipments,
        }
    return render(request, 'home/plants_equipments.html', context)


def gallery(request):
    site_setting = SiteSetting.objects.last()
    projects = Project.objects.all()

    context = {
        'siteSettings': site_setting,
        'projects': projects,
        }
    return render(request, 'home/gallery.html', context)