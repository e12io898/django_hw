from django.contrib import admin

from .models import Advertisement


@admin.register(Advertisement)
class AdvAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description',
                    'creator', 'status', 'created_at']
