# Generated by Django 4.2.9 on 2024-03-21 12:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Hit",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 3, 21, 12, 45, 40, 801735, tzinfo=datetime.timezone.utc)
                    ),
                ),
                ("reps", models.IntegerField()),
                ("weight", models.FloatField()),
                (
                    "exercise",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="calisthenics.exercise"),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
