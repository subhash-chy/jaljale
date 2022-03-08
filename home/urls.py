from django.urls import path

from .views import home, about_us, contact_us, services


app_name = 'home'
urlpatterns = [
    path('', home, name='index'),
    path('about-us', about_us, name='about-us'),
    path('contact-us', contact_us, name='contact-us'),
    path('our-services', services, name='services'),
]