import uuid
from django.db import models
from simple_history.models import HistoricalRecords

class Person(models.Model):
    """
    Represents an individual in the family tree.
    Includes cultural data, story generation, and lineage references.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Identity and naming
    full_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

    # Lifecycle
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    # Origins and family
    place_of_origin = models.CharField(max_length=255, blank=True)
    clan = models.CharField(max_length=100, blank=True)
    subclan = models.CharField(max_length=100, blank=True)
    father = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children_by_father')
    mother = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children_by_mother')

    # Cultural metadata
    aliases = models.JSONField(default=list, blank=True)
    cultural_notes = models.JSONField(default=dict, blank=True)

    # Visuals and narratives
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    biography = models.TextField(blank=True)
    story = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # Version history
    history = HistoricalRecords()

    def __str__(self):
        return self.full_name
