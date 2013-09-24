from django.contrib import admin

from .models import Question
from .models import Alternative


class AlternativeAdmin(admin.TabularInline):
    model = Alternative


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'date']
    list_filter = ['date',]
    inlines = [AlternativeAdmin]

admin.site.register(Question, QuestionAdmin)
