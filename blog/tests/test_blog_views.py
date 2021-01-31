from django.test import TestCase, Client
from django.urls import reverse

class TestBlogViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage = reverse('homepage')
        self.aboutpage = reverse('about')

    def test_get_homepage_status_code(self):
        response = self.client.get(self.homepage)
        self.assertEqual(response.status_code, 200)

    def test_get_homepage_rendered_template(self):
        response = self.client.get(self.homepage)
        self.assertTemplateUsed(response, 'home.html')

    def test_get_aboutpage_status_code(self):
        response = self.client.get(self.aboutpage)
        self.assertEqual(response.status_code, 200)

    def test_get_aboutpage_rendered_template(self):
        response = self.client.get(self.aboutpage)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_aboutpage_title(self):
        response = self.client.get(self.aboutpage)
        self.assertContains(response, 'About')
