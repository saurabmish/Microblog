from django.test import TestCase, Client
from django.urls import reverse

class TestUserViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register = reverse('register')

    def test_get_register_page_status_code(self):
        response = self.client.get(self.register)
        self.assertEqual(response.status_code, 200)

    def test_get_register_page_rendered_template(self):
        response = self.client.get(self.register)
        self.assertTemplateUsed(response, 'register.html')

    def test_get_register_page_form(self):
        response = self.client.get(self.register)
        self.assertContains(response, 'form')
