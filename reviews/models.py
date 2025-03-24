from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie
import uuid


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.movie)
