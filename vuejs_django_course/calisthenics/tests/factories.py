import random
from datetime import timedelta

import factory
from django.utils import timezone

from ..models import Exercise, Hit  # Update with the correct import path for your models
from ...users.tests.factories import UserFactory


class ExerciseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exercise

    name = factory.Sequence(lambda n: f"Exercise {n}")
    description = factory.Faker("text")
    active = True


def random_past_date(days=365):
    """
    Generates a random datetime between now and a specified number of days ago.
    :param days: Number of days in the past from which to generate a random date. Default is 365.
    """
    now = timezone.now()
    past_date = now - timedelta(days=days)
    random_date = past_date + timedelta(seconds=random.randint(0, int((now - past_date).total_seconds())))
    return random_date


class HitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hit

    exercise = factory.SubFactory(ExerciseFactory)
    date = factory.LazyFunction(lambda: random_past_date(365))
    reps = factory.Faker("pyint", min_value=1, max_value=100)
    weight = factory.Faker("pyfloat", left_digits=3, right_digits=2, positive=True)
    user = factory.SubFactory(UserFactory)  # Update the path to your UserFactory
