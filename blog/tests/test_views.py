from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment
import json



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.about_url = reverse('about')


    def test_blog_PostList(self):

        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html', 'index.html')

    def test_blog_AboutView(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html', 'about.html')




    

