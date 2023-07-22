"""Test for the Django admin modifications"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTest(TestCase):
    """Test Django admin"""

    def setUp(self):
        """Create user and Client"""
        self.client = Client()
        self.admin_user =get_user_model().objects.create_superuser(
            email = 'user@example.com',
            password = 'testpass123',
        )

        self.client.force_login(self.admin_user)
        self.user =get_user_model().objects.create_user(
            email = 'user1@example.com',
            password = 'testpass123',
            name = 'Test User',
        )

    def test_user_list(self):
        """Test that users are listed on page"""
        url = reverse('admin:core_user_changelist')
        res =self.client.get(url)

        self.assertTrue(res,self.user.name)
        self.assertTrue(res, self.user.email)
