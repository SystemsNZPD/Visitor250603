from celery import shared_task
from django.utils import timezone
from visitor_sign_in.models import Form  # Adjust the import based on your model location

@shared_task
def signout_all_visitors():
    now = timezone.now()
    updated = Form.objects.filter(sign_out__isnull=True).update(sign_out=now)
    return f"Successfully signed out {updated} visitors at {now}"
