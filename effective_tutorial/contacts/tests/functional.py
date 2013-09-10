from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory

from ..models import Contact
from ..views import ListContactView


class ContactTests(TestCase):

    def test_behavior_on_str_call(self):
        contact = Contact(first_name='John', last_name='Smith')
        self.assertEqual(str(contact), 'John Smith')


class ContactListViewTests(TestCase):
    """Contact list view tests."""

    def test_contacts_in_the_context(self):
        client = Client()
        response = client.get('/contacts/')
        self.assertEquals(list(response.context['object_list']), [])
        Contact.objects.create(first_name='foo', last_name='bar')
        response = client.get('/contacts/')
        self.assertEquals(response.context['object_list'].count(), 1)

    def test_contacts_in_the_context_request_factory(self):
        factory = RequestFactory()
        request = factory.get('/contacts/')
        response = ListContactView.as_view()(request)
        self.assertEquals(list(response.context_data['object_list']), [])
        Contact.objects.create(first_name='foo', last_name='bar')
        response = ListContactView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
