from django.forms import ModelForm
from django import forms
from MoonTrekStories.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['commentor', 'comment']
        widgets = { 
            'comment': forms.Textarea(attrs={'cols': 80, 'rows': 4}), 
            }