from django.db import models
import uuid
from people.models import Person
from simple_history.models import HistoricalRecords

class Marriage(models.Model):
    """
    Represents a marriage or union between two people.
    Supports polygamy, remarriage, and traditional vs civil tracking.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    husband = models.ForeignKey(
        Person,
        related_name='marriages_as_husband',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    wife = models.ForeignKey(
        Person,
        related_name='marriages_as_wife',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    marriage_type = models.CharField(
        max_length=20,
        choices=[
            ('traditional', 'Traditional'),
            ('civil', 'Civil'),
            ('religious', 'Religious'),
            ('customary', 'Customary'),
            ('other', 'Other')
        ],
        default='traditional'
    )

    notes = models.TextField(blank=True)
    history = HistoricalRecords()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.husband} & {self.wife} ({self.marriage_type})"
