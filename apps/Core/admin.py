from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')
    search_fields = ('title', 'subtitle', 'content')
    list_filter = ('date_created', 'author')
