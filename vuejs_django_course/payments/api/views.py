from rest_framework.generics import ListAPIView

from vuejs_django_course.payments.api.serializers import RecurrentPaymentSerializer
from vuejs_django_course.payments.models import RecurrentPayment


class RecurrentPaymentListAPIView(ListAPIView):
    serializer_class = RecurrentPaymentSerializer
    queryset = RecurrentPayment.objects.all()
