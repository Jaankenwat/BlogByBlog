from django.contrib import admin
from .models import Blog
from tinymce.widgets import TinyMCE
from django.db import models

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
admin.site.register(Blog, BlogAdmin)
