from django.test import TestCase
from app.models import Post

class PostTestCase(TestCase):
    def testPost(self):

        post = Post(title="My Title", description="Burb", wiki="Post Body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "Burb")
        self.assertEqual(post.wiki, "Post Body")