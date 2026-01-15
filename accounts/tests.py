from django.test import TestCase
from .models import User, OTPVerification

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email="test@example.com", password="12345")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("12345"))

class OTPTest(TestCase):
    def test_otp_creation(self):
        user = User.objects.create_user(email="otp@example.com", password="12345")
        otp = OTPVerification.objects.create(user=user)
        self.assertEqual(len(otp.code), 6)
        self.assertFalse(otp.is_used)
