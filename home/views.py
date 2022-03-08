from django.shortcuts import render, redirect

from project.models import Project

from .models import Banner
from setting.models import SiteSetting
from testimonial.models import Testimonial
from about_us.models import AboutUs
from contact.models import ContactUs


def home(request):
    banner = Banner.objects.last()
    logo = Banner.objects.last()
    site_setting = SiteSetting.objects.last()
    testimonials = Testimonial.objects.all()
    about_us = AboutUs.objects.last()
    projects = Project.objects.all()

    context = {
        'banner': banner,
        'logo': logo,
        'siteSettings': site_setting,
        'testimonials': testimonials,
        'aboutUs': about_us,
        'projects': projects,
    }
    return render(request, 'home/index.html', context)


def about_us(request):
    logo = Banner.objects.last()
    site_setting = SiteSetting.objects.last()
    about_us = AboutUs.objects.last()

    context = {
        'logo': logo,
        'siteSettings': site_setting,
        'aboutUs': about_us,

    }
    return render(request, 'home/about_us.html', context )


# def contact_us(request):
#     logo = Banner.objects.last()
#     site_setting = SiteSetting.objects.last()

#     context = {
#         'logo': logo,
#         'siteSettings': site_setting,
#     }
#     return render(request, 'home/contact_us.html', context )

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
    logo = Banner.objects.last()
    site_setting = SiteSetting.objects.last()

    context = {
        'logo': logo,
        'siteSettings': site_setting,
        }
    return render(request, 'home/services.html', context)