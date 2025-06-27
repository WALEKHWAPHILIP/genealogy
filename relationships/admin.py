from django.contrib import admin
from .models import Marriage

@admin.register(Marriage)
class MarriageAdmin(admin.ModelAdmin):
    """
    Admin interface for managing marriages with lineage and cultural insights.
    """
    list_display = ('husband', 'wife', 'marriage_type', 'start_date', 'end_date', 'created_at')
    list_filter = ('marriage_type', 'start_date', 'end_date')
    search_fields = ('husband__full_name', 'wife__full_name', 'notes')
    date_hierarchy = 'start_date'
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('husband', 'wife', 'marriage_type', 'start_date', 'end_date')
        }),
        ('Additional Info', {
            'fields': ('notes', 'created_at'),
            'classes': ('collapse',)
        }),
    )
