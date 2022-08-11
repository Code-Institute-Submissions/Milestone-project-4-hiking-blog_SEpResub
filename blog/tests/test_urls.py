from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from blog.views import PostList, AboutView


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_about_url_resolves(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AboutView)






