from django.urls import path

from .views import ongoing_projects


app_name = 'project'
urlpatterns = [
    path('ongoing', ongoing_projects, name='ongoing_projects'),

]