from django import forms
from .models import Post
from django.core.exceptions import NON_FIELD_ERRORS


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image', 'content']
       