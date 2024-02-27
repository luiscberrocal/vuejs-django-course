from django_filters import rest_framework as filters
from vuejs_django_course.payments.models import Payment


class PaymentFilter(filters.FilterSet):
    min_date = filters.DateTimeFilter(field_name='created', lookup_expr='gte')
    max_date = filters.DateTimeFilter(field_name='created', lookup_expr='lte')

    class Meta:
        model = Payment
        fields = (
            'recurrent_payment',
        )
