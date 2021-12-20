from celery import shared_task
from .models import UpVote


@shared_task
def reset_upvotes():
    UpVote.objects.all().delete()
    return "Upvotes reseted!"