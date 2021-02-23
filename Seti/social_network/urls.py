from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('download/', views.DownloadView.as_view(), name='download'),
    path('inform_comp/', views.inform_comp, name='inform_comp'),
    path('upload/', views.upload, name='upload'),
    path('', views.index),
    path('<str:room_name>/', views.room, name='room'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)