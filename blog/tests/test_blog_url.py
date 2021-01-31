from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import homepage, about

class TestBlogUrls(SimpleTestCase):

    def test_homepage_url_resolution(self):
        url = reverse('homepage')
        self.assertEqual(resolve(url).func, homepage)

    def test_aboutpage_url_resolution(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)
