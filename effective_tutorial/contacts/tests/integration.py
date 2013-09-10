from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from ..models import Contact


class ContactListIntegrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(ContactListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ContactListIntegrationTests, cls).tearDownClass()

    def test_contact_listed(self):
        Contact.objects.create(first_name='foo', last_name='bar')
        self.selenium.get('%s%s' % (self.live_server_url, '/contacts/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.contact')[0].text,
            'foo bar'
        )

    def test_add_contact_linked(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/contacts/'))
        self.assert_(
            self.selenium.find_element_by_link_text('add contact')
        )

    def test_add_contact(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/contacts/new/'))
        find_element = self.selenium.find_element_by_id
        find_element('id_first_name').send_keys('test')
        find_element('id_last_name').send_keys('contact')
        find_element('id_email').send_keys('test@example.com')
        find_element('save_contact').click()
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.contact')[-1].text,
            'test contact'
        )
