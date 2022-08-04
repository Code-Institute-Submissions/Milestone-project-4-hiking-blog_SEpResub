from django.test import TestCase
from .forms import CommentForm
# Create your tests here.


class HikeBlogTest(TestCase):

    def test_home_view(self):
        """This checks the home view page has loaded correctly"""
        res = self.client.get('/index.html/')
        assert b'Top Hikes in Chile' in res.content
        assert b'Welcome to HikeIt' in res.content