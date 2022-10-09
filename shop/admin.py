from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class GabardinAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'category', 'get_html_photo', 'title', 'color', 'quantity', 'price', 'available', 'time_update')
    list_display_links = ('title', 'color',)
    search_fields = ('color', 'quantity')
    list_editable = ('price', 'quantity', 'available')
    list_filter = ('category', 'available')
    prepopulated_fields = {"slug": ("color",)}
    fields = ('title', 'color', 'slug', 'quantity', 'price', 'photo', 'get_html_photo', 'category', 'available', 'time_update')
    readonly_fields = ('get_html_photo', 'time_update')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=40 height=40>")

    get_html_photo.short_description = "Картинка"


admin.site.register(Gabardin, GabardinAdmin, )
