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

    def test_post_registration_success_message(self):
        pass

    def test_post_registration_success_redirection(self):
        pass

    def test_get_profile_page_logged_in_status_code(self):
        pass

    def test_get_profile_page_logged_in_rendered_template(self):
        pass

    def test_get_profile_page_not_logged_in_status_code(self):
        pass

    def test_get_profile_page_not_logged_in_rendered_template(self):
        pass
