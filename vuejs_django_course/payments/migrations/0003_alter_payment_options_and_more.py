# Generated by Django 4.2.9 on 2024-02-26 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0002_alter_payment_options_payment_comments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={"ordering": ("-date",)},
        ),
        migrations.AlterField(
            model_name="payment",
            name="recurrent_payment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="payments", to="payments.recurrentpayment"
            ),
        ),
    ]
