from django.contrib import admin

from .models import RecurrentPayment, Payment


# Register your models here.

@admin.register(RecurrentPayment)
class RecurrentPaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date_due', 'is_active', 'is_amount_fixed')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'is_amount_fixed', 'date_due')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('recurrent_payment', 'date', 'amount')
    search_fields = ('recurrent_payment__name', 'recurrent_payment__description')
    list_filter = ('date', 'recurrent_payment__is_active', 'recurrent_payment__is_amount_fixed')
