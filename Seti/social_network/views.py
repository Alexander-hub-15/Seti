from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User


class AuthView(ListView):
    user = User
    template_name = 'social_networks/login.html'


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'social_networks/model_form_upload.html')