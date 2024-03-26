from datetime import date
from typing import Any

from django.db import models

from vuejs_django_course.users.models import User


class HitManager(models.Manager):

    def get_stats(self, user: User, event_date: date) -> Any:
        return self.filter(
            user=user,
            date__year=event_date.year,
            date__month=event_date.month,
            date__day=event_date.day
        ).aggregate(
            total_reps=models.Sum('reps'),
        )
