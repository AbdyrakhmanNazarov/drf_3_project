from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OTPVerification

@receiver(post_save, sender=OTPVerification)
def log_otp_creation(sender, instance, created, **kwargs):
    if created:
        print(f"Создан OTP для {instance.user.email}: {instance.code}")