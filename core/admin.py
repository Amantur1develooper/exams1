from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class ImageStackedInline(admin.StackedInline):
    model = Image
    extra = 3
    
    
class ProductAtributeStackedInline(admin.StackedInline):
    model = ProductAtribute
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags')
    filter_horizontal = ('tags',)
    raw_id_fields = ('category',)
    inlines = (ProductAtributeStackedInline, ImageStackedInline)


admin.site.register(Tag)


admin.site.register(Category)
