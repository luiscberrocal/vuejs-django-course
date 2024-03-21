from django.db import models
from model_utils.models import TimeStampedModel

from vuejs_django_course.core.models import AuditableModel


# Create your models here.
class RecurrentPayment(AuditableModel, TimeStampedModel):
    name = models.CharField(max_length=100,
                            help_text='Name of the payment. For example: Life insurance, Cellphone, etc.')
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Amount of the payment')
    description = models.TextField(null=True, blank=True, help_text='Description of the payment')
    date_due = models.DateField(help_text='Date when the payment is due')
    is_active = models.BooleanField(default=True, help_text='Is the payment active?')
    is_amount_fixed = models.BooleanField(default=True, help_text='Is the amount fixed?')

    def __str__(self):
        return self.name


class Payment(AuditableModel, TimeStampedModel):
    recurrent_payment = models.ForeignKey(RecurrentPayment, on_delete=models.CASCADE, related_name='payments')
    date = models.DateTimeField(help_text='Date of the payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Amount of the payment')
    comments = models.TextField(null=True, blank=True, help_text='Comments of the payment')

    def __str__(self):
        return f'{self.recurrent_payment.name} - {self.date}'

    class Meta:
        ordering = ('-date',)
