from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from cards.views import CardCollection


class PostCardTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='john',
            password='john123pwd',
            email='john@gmail.com'  # Add an email address
        )


    def tearDown(self):
        self.user.delete()

    #method to avoid code duplication
    def post_card(self, url, title, description, status):
        data = {
            'title': title,
            'description': description,
            'status': status
        }
        response = self.client.post(url, data, format='json')
        return response


    def test_post_card_anonymously(self):
        url = reverse(CardCollection.name)
        response = self.post_card(url, 'Sprint1', 'new sprint', 1)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_post_card(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(CardCollection.name)
        response = self.post_card(url, 'Create automation', 'automate new functionality',0)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'Create automation'
        assert response.data['description'] == 'automate new functionality'
        assert response.data['status_text'] == 'to-do'
        assert response.data['owner'] == 'john@gmail.com'
