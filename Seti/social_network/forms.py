from django import forms
from django.core.exceptions import ValidationError

from social_network.models import Questions


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['slug', 'text']
        widgets = {
            # 'name_person': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            # 'name_cat': forms.MultiValueField(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug is not be "Create"')
        return new_slug
