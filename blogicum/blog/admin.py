from django.contrib import admin

from .models import Category
from .models import Location
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_published')
    list_filter = ('is_published', 'pub_date', 'author', 'category')
    search_fields = ('title', 'text')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
