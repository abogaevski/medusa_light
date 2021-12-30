from django.utils import timezone
from django.db import models

from common.models import TimestampedModel


class News(TimestampedModel):
    subject = models.CharField('Title', max_length=255)
    content = models.TextField('Content')
    date = models.DateField('Date', default=timezone.now)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-date']
