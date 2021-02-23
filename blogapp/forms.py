from django import forms
from blogapp.models import Comment, Blog


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
