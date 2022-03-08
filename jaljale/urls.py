from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static, serve


patterns = [
    path('', include('home.urls', namespace="home")),
    path('project/', include('project.urls', namespace="project")),
]

extrapatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    staticpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    staticpatterns = [
        re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns = patterns + staticpatterns + extrapatterns
