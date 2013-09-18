import logging

from django import forms


logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data.split(' ')) < 2:
            raise forms.ValidationError('First and Last names seperated by space!')
        else:
            return data

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print 'Sending e-mail to %s ...' % self.cleaned_data['name']
