from .models import reviews
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = ('name', 'email', 'content')
