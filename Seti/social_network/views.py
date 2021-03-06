import json

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.views.generic import ListView

from social_network.forms import QuestionForm
from social_network.models import Document, Questions


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


def posts(request):
    data = {
        'posts': Questions.objects.all()
    }
    return render(request, 'social_networks/posts.html', data)


def create_question(request):
    error = ''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post')
        else:
            error = 'Форма была неверной'

    form = QuestionForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'social_networks/create.html', data)
