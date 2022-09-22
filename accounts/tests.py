from django.test import TestCase
# User Model import taken from default specified in settings
from django.contrib.auth import get_user_model
# Create your tests here.
class CustomUserTests(TestCase):
    """Tests on our primary user model"""
    def test_create_user(self):
        """Check if a simple user created is correct"""
        User = get_user_model()
        user = User.objects.create_user(
            username = "will", email = "will@email.com", password = "testpass123"
        )
        self.assertEqual(user.username,"will")
        self.assertEqual(user.email,"will@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    def test_create_superuser(self):
        User = get_user_model()
        adminUser = User.objects.create_superuser(
            username = "superadmin", email = "superadmin@email.com",password = "testpass123"
        )
        self.assertEqual(adminUser.username,"superadmin")
        self.assertEqual(adminUser.email,"superadmin@email.com")
        self.assertTrue(adminUser.is_active)
        self.assertTrue(adminUser.is_staff)
        self.assertTrue(adminUser.is_superuser)