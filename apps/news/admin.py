from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'short_description', 'date', 'active']
    list_display = ['title', 'date', 'active']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News, NewsAdmin)
