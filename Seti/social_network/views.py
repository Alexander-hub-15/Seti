from aioredis.commands import generic
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

import json

from social_network.models import Document


class AuthView(ListView):
    user = User
    template_name = 'social_networks/login.html'


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'social_networks/model_form_upload.html')


class DownloadView(ListView):
    model = Document
    fields = ['description', 'document']
    template_name = 'social_networks/download.html'


def index(request):
    return render(request, 'social_networks/base.html')


def room(request, room_name):
    return render(request, 'social_networks/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def inform_comp(request):
    import platform
    data = {
        'inform': platform.processor()
    }
    return render(request, 'social_networks/inform_comp.html', data)
