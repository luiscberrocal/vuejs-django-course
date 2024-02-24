from django.contrib import admin

from .models import RecurrentPayment, Payment


class AuditableAdminMixin:
    readonly_fields = ('created_by', 'modified_by')

    def save_model(self, request, obj, form, change):
        if obj.pk:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
        super(AuditableAdminMixin, self).save_model(request, obj, form, change)


# Register your models here.

@admin.register(RecurrentPayment)
class RecurrentPaymentAdmin(AuditableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'amount', 'date_due', 'is_active', 'is_amount_fixed')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'is_amount_fixed', 'date_due')


@admin.register(Payment)
class PaymentAdmin(AuditableAdminMixin, admin.ModelAdmin):
    list_display = ('recurrent_payment', 'date', 'amount')
    search_fields = ('recurrent_payment__name', 'recurrent_payment__description')
    list_filter = ('date', 'recurrent_payment__is_active', 'recurrent_payment__is_amount_fixed')
