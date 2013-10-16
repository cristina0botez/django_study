from django import forms

from experiments.models import Author


__all__ = ['AuthorForm']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['last_accessed', 'created_by']