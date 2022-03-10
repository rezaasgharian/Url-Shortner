from django.contrib.auth.models import User
from django.test import TestCase

from main.models import ShortURL


class TestCreateUrlTest(TestCase):
    def test_anonymous_create(self):
        self.assertEqual(0, ShortURL.objects.count())

        response = self.client.post(
            '/api/urls/',
            {'url': 'http://google.com/'},
            content_type='application/json',
            HTTP_HOST='testserver',
        )
        data = response.data

        new_short_url = ShortURL.objects.get()
        self.assertEqual('http://google.com/', data['url'])
        self.assertEqual(f'http://testserver/r/?id={new_short_url.short_id}', data['alias'])
        self.assertIsNone(new_short_url.author)

    def test_create_with_author(self):
        user = User.objects.create_user(username='testuser', password='123456')
        self.client.login(username='testuser', password='123456')

        self.client.post(
            '/api/urls/',
            {'url': 'http://google.com/'},
            content_type='application/json',
            HTTP_HOST='testserver',
        )
        new_short_url = ShortURL.objects.get()
        self.assertEqual(user, new_short_url.author)        

