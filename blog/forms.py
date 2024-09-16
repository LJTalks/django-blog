from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': '',  # This remoives the label, no part of the tutorial
        }
