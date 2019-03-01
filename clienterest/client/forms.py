from django import forms

from .models import Post

class RatingForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','calificacion')