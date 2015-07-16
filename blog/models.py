from django.db import models
from django_markdown.models import MarkdownField

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = MarkdownField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    objects = EntryQuerySet.as_manager()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Blog Entry'
        verbose_name_plural='Blog Entries'
        ordering = ['-created']

