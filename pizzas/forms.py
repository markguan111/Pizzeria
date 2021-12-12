from django import forms
from django.forms import fields
from django import forms

from .models import Comment ,Image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        Labels = {'name':''}

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('pizza', 'image')