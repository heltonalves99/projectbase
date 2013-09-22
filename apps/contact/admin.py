# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = list_display

admin.site.register(Contact, ContactAdmin)
