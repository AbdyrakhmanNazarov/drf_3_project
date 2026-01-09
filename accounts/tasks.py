from celery import shared_task
from django.utils import timezone
from .models import OTPVerification

@shared_task
def delete_expired_otps():
    expired = OTPVerification.objects.filter(
        is_used=False,
        created_at__lt=timezone.now() - timezone.timedelta(minutes=5)
    )
    count = expired.count()
    expired.delete()
    return f"{count} OTP удалено"