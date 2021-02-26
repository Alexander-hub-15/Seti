from django import forms
from django.core.exceptions import ValidationError

from social_network.models import Questions


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['text']
        widgets = {
            'text': forms.Textarea(),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug is not be "Create"')
        return new_slug
