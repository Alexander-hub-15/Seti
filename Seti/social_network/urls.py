from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat)
    path('', views.model_form_upload, name='upload'),
]