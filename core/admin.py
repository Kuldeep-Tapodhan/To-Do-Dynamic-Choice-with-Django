from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Status, Task


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin configuration for CustomUser with extra profile fields."""
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    # Add custom fields to the edit form
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('phone', 'bio')}),
    )
    # Add custom fields to the add form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Profile', {'fields': ('email', 'first_name', 'last_name', 'phone', 'bio')}),
    )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'modified_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'modified_at']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'priority', 'is_completed', 'due_date', 'created_at']
    list_filter = ['status', 'priority', 'is_completed', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    readonly_fields = ['created_at', 'modified_at']
    list_editable = ['priority', 'is_completed']