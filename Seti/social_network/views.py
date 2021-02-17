from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User

from social_network.forms import DocumentForm


class AuthView(ListView):
    user = User
    template_name = 'social_networks/auth.html'


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })