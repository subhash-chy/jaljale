from django.urls import path

from .views import ongoing_projects, completed_projects, view_project


app_name = 'project'
urlpatterns = [
    path('ongoing', ongoing_projects, name='ongoing_projects'),
    path('completed', completed_projects, name='completed_projects'),
    path('<int:id>', view_project, name='view_project'),
]