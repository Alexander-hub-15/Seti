from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)