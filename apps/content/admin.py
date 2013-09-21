from django.contrib import admin

from .models import Content


class ContentAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'father', 'active']
    list_filter = list_display
    search_fields = ['active']

admin.site.register(Content, ContentAdmin)
