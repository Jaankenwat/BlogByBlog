from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    content = HTMLField()  # Rich Text Field using TinyMCE

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Auto-generate slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
