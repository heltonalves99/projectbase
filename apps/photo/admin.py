from django.contrib import admin

from .models import Gallery
from .models import Image


class ImageAdmin(admin.TabularInline):
    model = Image


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'active', 'upload_photos']
    list_filter = ['title', 'date', 'active']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageAdmin]

    def upload_photos(self, obj):
        return '<a href="/fileupload/image/%s" class="open-gallery">Adicionar Imagens</a>' % (obj.id)
    upload_photos.allow_tags = True
    upload_photos.short_description = 'Adicionar Imagens'

    class Media:
        js = ("/static/js/admin_gallery.js",)

admin.site.register(Gallery, GalleryAdmin)
