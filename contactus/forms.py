from django import forms
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.models import User
from django.core.validators import ValidationError
from .models import Contact


class ContactUsForm(forms.Form):

    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea())

    def clean(self):
        name = self.cleaned_data.get('name')
        subject = self.cleaned_data.get('subject')

        # if 'a' in name:
        #     self.add_error('name', 'a can not be in name    ')

        if name == subject:
            raise ValidationError('name and subject are same', code='name_message_same')
