from django.db import models
import uuid
from people.models import Person
from simple_history.models import HistoricalRecords





class EventType(models.Model):
    """
    Master list of event types used to describe life, cultural, or spiritual events.
    Enables dynamic, category-based classification and extensibility.
    """
    code = models.SlugField(max_length=50, unique=True, help_text="Unique code identifier (e.g. birth, migration)")
    label = models.CharField(max_length=100, help_text="Human-readable label (e.g. Birth, Graduation)")
    description = models.TextField(blank=True, help_text="Optional description or narrative usage context")
    category = models.CharField(
        max_length=50,
        blank=True,
        help_text="Broad category for grouping (e.g. Life, Spiritual, Migration, etc.)"
    )
    is_active = models.BooleanField(default=True, help_text="Control availability without deleting")

    class Meta:
        ordering = ['category', 'label']
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"

    def __str__(self):
        return f"{self.label} ({self.category})"



class Event(models.Model):
    """
    Represents a significant event in a person's life (e.g., migration, education, initiation).
    Customizable and extensible for cultural richness.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='events'
    )

    event_type = models.ForeignKey(
        EventType,
        on_delete=models.PROTECT,
        related_name='events'
    )

    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    metadata = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.person.full_name} - {self.event_type.label} ({self.date})"
