from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Post

class TestBlogModels(TestCase):

    def setUp(self):
        author = User.objects.create(username='TestUser1')
        self.post = Post.objects.create(
                        author=author,
                        title='Test Post Title 1',
                        content='Test content for title 1'
                    )

    def test_blog_post_author_type(self):
        self.assertIsInstance(self.post.author, User)

    def test_blog_post_title_type(self):
        self.assertIsInstance(self.post.title, str)

    def test_blog_post_content_type(self):
        self.assertIsInstance(self.post.content, str)

    def test_blog_published_timestamp(self):
        self.assertIsInstance(self.post.published, datetime)

    def test_blog_author_label(self):
        author_field = Post._meta.get_field('author').verbose_name
        self.assertEqual(author_field, "author")

    def test_blog_title_label(self):
        title_field = Post._meta.get_field('title').verbose_name
        self.assertEqual(title_field, "title")

    def test_blog_content_label(self):
        content_field = Post._meta.get_field('content').verbose_name
        self.assertEqual(content_field, "content")

    def test_blog_title_max_length(self):
        title_field_length = Post._meta.get_field('title').max_length
        self.assertEqual(title_field_length, 100)

    def test_published_blog_data(self):
        post_metadata = Post.objects.get(title='Test Post Title 1')
        expected_data = f"{post_metadata.author} {post_metadata.title} {post_metadata.content}"
        self.assertEqual(expected_data, str(post_metadata))
