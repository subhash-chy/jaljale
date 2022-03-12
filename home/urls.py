from django.urls import path

from .views import home, about_us, contact_us, services, plants_equipments, gallery


app_name = 'home'
urlpatterns = [
    path('', home, name='index'),
    path('about-us', about_us, name='about-us'),
    path('contact-us', contact_us, name='contact-us'),
    path('our-services', services, name='services'),
    path('plants-and-equipments', plants_equipments, name='plants_equipments'),
    path('gallery', gallery, name='gallery'),
]