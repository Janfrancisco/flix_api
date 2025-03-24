from django.db import models
import uuid

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('GBR', 'Britânico'),
    ('ISR', 'Israelense'),
    ('ARG', 'Argentina'),
    ('COL', 'Colombia'),
    ('MEX', 'Mexico'),
    ('ESP', 'España'),
    ('FRA', 'Francia'),
)


class Actor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
