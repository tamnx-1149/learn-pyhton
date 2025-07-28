import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn.settings')
django.setup()

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Article
from django.contrib.auth.models import User


class ArticleViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', email='test@email.com', password='123456')
        response = self.client.post('/api/login/', {'email': 'test@email.com', 'password': '123456'})
        access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        # Tạo bài viết mẫu để test
        self.article = Article.objects.create(
            title="Test Article",
            slug="test-article",
            body="Nội dung test",
            author=self.user

        )
        self.list_url = reverse('article-list-create')  # URL cho list articles
        self.detail_url = reverse('article-detail', args=[self.article.slug])  # URL detail

    def test_get_article_list(self):
        # Test GET lấy danh sách bài viết
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_article_detail(self):
        # Test GET lấy chi tiết bài viết
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug'], self.article.slug)

    def test_post_article(self):
        # Test tạo mới bài viết
        data = {
            "title": "New Article",
            "slug": "new-article",
            "content": "Nội dung mới",
            "body": "body",
            "author": self.user
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_article(self):
        # Test cập nhật bài viết
        data = {
            "title": "Updated Title",
            "slug": "test-article",  # slug giữ nguyên
            "content": "Updated content",
            "body": "body",
            "author": self.user
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, "Updated Title")

    def test_delete_article(self):
        # Test xóa bài viết
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
