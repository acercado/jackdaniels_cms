from django.utils import timezone
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    banner = models.CharField(max_length=200)
    publish_duration = models.DateTimeField()
    posted_by = models.ForeignKey('cms.MyUser')
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'News'