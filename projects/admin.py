from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'domain', 'teacher', 'status', 'max_students', 'accepted_count', 'created_at']
    list_filter = ['status', 'domain']
    search_fields = ['title', 'description', 'teacher__email']
    readonly_fields = ['created_at', 'updated_at']