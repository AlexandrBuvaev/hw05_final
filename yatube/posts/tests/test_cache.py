from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Comment, Group, Post

User = get_user_model()


class PostContextTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='TestUser')
        cls.group = Group.objects.create(
            title='Test',
            slug='test_slug',
            description='Test group'
        )
        cls.post = Post.objects.create(
            text='Тестовый текст',
            author=cls.user,
            group=cls.group,
        )
        cls.comment = Comment.objects.create(
            text='test comment',
            author=cls.post.author,
            post=cls.post
        )

    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_index_page_cache(self):
        Post.objects.create(text='Тестовый текст',
                            author=self.user,
                            group=self.group
                            )
        response = self.client.get(reverse('posts:index'))
        last_object = Post.objects.latest('id')
        last_object.delete()
        response_cache = self.client.get(reverse('posts:index'))
        cache.clear()
        response_no_cache = self.client.get(reverse('posts:index'))
        self.assertEqual(response.content, response_cache.content)
        self.assertNotEqual(response.content, response_no_cache.content)
