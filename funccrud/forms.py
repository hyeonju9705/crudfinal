from django import forms
from .models import Blog, Comment

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['category','title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)