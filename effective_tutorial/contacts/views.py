from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView

from .models import Contact


class ListContactView(ListView):
    queryset = Contact.objects.order_by('last_name')
    template_name = 'contact_list.html'


class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts_list')