from django.db import models
from model_utils.models import TimeStampedModel

from vuejs_django_course.core.models import AuditableModel


# Create your models here.
class Exercise(AuditableModel, TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Hit(AuditableModel, TimeStampedModel):
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    date = models.DateTimeField()
    reps = models.IntegerField()
    weight = models.FloatField()
    user = models.ForeignKey("users.User", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.exercise.name} - {self.date}"
