from .models import Comment
from django import forms
from .models import Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'Content', 'featured_image', 'excerpt', 'status', 'likes',]
