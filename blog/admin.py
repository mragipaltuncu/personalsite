from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from blog import models

class EntryAdmin(MarkdownModelAdmin):
    list_display = ('title','created')
    prepopulated_fields = {'slug':('title',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)


admin.site.register(models.Entry,EntryAdmin)
admin.site.register(models.Tag,TagAdmin)