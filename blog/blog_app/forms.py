from django import forms
from .models import Blog, Comment

class CreateForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=["description","blog_content","cover_photo","populer"]


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["name","content"]