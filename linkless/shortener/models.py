import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel


class ShortenedLink(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original_url = models.URLField()
    short_code = models.SlugField(unique=True)
    expiry_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.short_code

    def is_expired(self):
        return self.expiry_date and timezone.now() > self.expiry_date

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_unique_short_code()
        super(ShortenedLink, self).save(*args, **kwargs)

    def generate_unique_short_code(self):
        code = str(uuid.uuid4())[:8]
        while ShortenedLink.objects.filter(short_code=code).exists():
            code = str(uuid.uuid4())[:8]
        return code
