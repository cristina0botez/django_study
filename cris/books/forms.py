from django import forms

from .models import Author


__all__ = ['AuthorForm']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['last_accessed', 'created_by']


class AuthorInterestForm(forms.Form):
    message = forms.CharField(required=True)