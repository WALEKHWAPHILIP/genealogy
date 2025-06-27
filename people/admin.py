from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """
    Admin UI configuration for Person.
    Optimized for clarity, cultural context, and storytelling.
    """
    list_display = ('full_name', 'clan', 'place_of_origin', 'gender', 'date_of_birth')
    search_fields = ('full_name', 'first_name', 'middle_name', 'surname', 'aliases')
    list_filter = ('clan', 'gender', 'place_of_origin')
    readonly_fields = ('story', 'created_at')

    fieldsets = (
        ('Core Identity', {
            'fields': ('full_name', 'first_name', 'middle_name', 'surname', 'gender', 'photo')
        }),
        ('Lineage & Origin', {
            'fields': ('father', 'mother', 'clan', 'subclan', 'place_of_origin')
        }),
        ('Cultural Metadata', {
            'classes': ('collapse',),
            'fields': ('aliases', 'cultural_notes')
        }),
        ('Narrative & Life Events', {
            'fields': ('date_of_birth', 'date_of_death', 'biography', 'story')
        }),
        ('System Info', {
            'fields': ('created_at',)
        }),
    )
