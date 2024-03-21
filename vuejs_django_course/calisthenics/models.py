from django.db import models
from django.utils import timezone


# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Hit(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now())
    reps = models.IntegerField()
    weight = models.FloatField()
    user = models.ForeignKey("users.User", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.exercise.name} - {self.date}"
