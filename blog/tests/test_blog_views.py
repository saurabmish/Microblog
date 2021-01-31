import json

from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Post

class TestBlogViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.aboutpage_url = reverse('about')

    def test_get_homepage_status_code(self):
        response = self.client.get(self.homepage_url)
        self.assertEqual(response.status_code, 200)

    def test_get_homepage_rendered_template(self):
        response = self.client.get(self.homepage_url)
        self.assertTemplateUsed(response, 'home.html')

    def test_get_aboutpage_status_code(self):
        response = self.client.get(self.aboutpage_url)
        self.assertEqual(response.status_code, 200)

    def test_get_aboutpage_rendered_template(self):
        response = self.client.get(self.aboutpage_url)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_aboutpage_title(self):
        response = self.client.get(self.aboutpage_url)
        self.assertContains(response, 'About')
