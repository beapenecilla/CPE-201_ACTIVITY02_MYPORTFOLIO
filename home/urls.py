from django.urls import path

from djangoProject import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/about', views.about, name='about'),
    path('/project', views.project, name='project'),
    path('/contact', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
