from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_mommy import mommy

from feedsapi.models import Feed


class FeedTests(APITestCase):

    def test_should_get_feeds(self):
        feeds_count = 10
        mommy.make(Feed, feeds_count)

        url = reverse('feeds_list')
        response = self.client.get(url)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["count"], feeds_count)

    def test_should_post_feed(self):
        feed_count = 4
        mommy.make(Feed, feed_count)
        new_feed = {
            "title": "Test",
            "guid": "Test-asdf-2334-sdf",
            "link": "http://test.com",
            "description": "Test",
            "published": "Test",
            "tag": "AAPL"
        }

        url = reverse('feeds_list')
        response = self.client.post(url, data=new_feed)
        response_data = response.data

        self.assertEqual(response_data["title"], "Test")
        self.assertEqual(response_data["guid"], "Test-asdf-2334-sdf")
        self.assertEqual(response_data["link"], "http://test.com")
        self.assertEqual(response_data["description"], "Test")
        self.assertEqual(response_data["published"], "Test")
        self.assertEqual(response_data["tag"], "AAPL")

    def test_should_get_feed_by_id(self):
        feed = mommy.make(Feed)

        url = reverse('feed', args=[feed.id])
        response = self.client.get(url)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["title"], feed.title)

    def test_should_update_feed_by_id(self):
        feed = mommy.make(Feed, title="Not Updated Yet")
        update_data = {
            "title": "Updated title",
            "guid": "Test-asdf-2334-sdf",
            "link": "http://test.com",
            "description": "Test",
            "published": "Test",
            "tag": "AAPL"
        }

        url = reverse('feed', args=[feed.id])
        response = self.client.put(url, update_data)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["title"], "Updated title")

    def test_should_delete_feed_by_id(self):
        feed = mommy.make(Feed)

        url = reverse('feed', args=[feed.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
