from celery import shared_task
from django.utils import timezone
from .models import OTPVerification
import logging

logger = logging.getLogger(__name__)

@shared_task
def delete_expired_otps():
    expired = OTPVerification.objects.filter(
        is_used=False,
        created_at__lt=timezone.now() - timezone.timedelta(minutes=5)
    )
    count = expired.count()
    if count > 0:
        expired.delete()
        logger.info(f"{count} OTP удалено")
    return f"{count} OTP удалено"
