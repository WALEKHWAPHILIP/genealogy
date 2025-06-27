from django.contrib import admin
from .models import EventType
from .models import Event

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    """
    Admin interface for managing genealogical event types with cultural categories.
    """
    list_display = ('label', 'code', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('label', 'code', 'description')
    ordering = ('category', 'label')
    list_editable = ('is_active',)

    fieldsets = (
        (None, {
            'fields': ('code', 'label', 'category', 'description', 'is_active')
        }),
    )





@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin interface for managing life and cultural events linked to people and event types.
    """
    list_display = ('person', 'event_type', 'date', 'location', 'created_at')
    list_filter = ('event_type__category', 'event_type', 'date')
    search_fields = ('person__full_name', 'event_type__label', 'location', 'description')
    autocomplete_fields = ('person', 'event_type')
    date_hierarchy = 'date'
    ordering = ('-date',)

    fieldsets = (
        (None, {
            'fields': ('person', 'event_type', 'date', 'location', 'description', 'metadata')
        }),
        ('Audit Trail', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)
