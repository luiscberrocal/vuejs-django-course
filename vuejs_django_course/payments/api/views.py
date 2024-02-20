from rest_framework.generics import ListAPIView, RetrieveAPIView

from vuejs_django_course.payments.api.serializers import RecurrentPaymentSerializer
from vuejs_django_course.payments.models import RecurrentPayment


class RecurrentPaymentListAPIView(ListAPIView):
    serializer_class = RecurrentPaymentSerializer
    queryset = RecurrentPayment.objects.all()


recurrent_payment_list_api_view = RecurrentPaymentListAPIView.as_view()


class RecurrentPaymentDetailAPIView(RetrieveAPIView):
    serializer_class = RecurrentPaymentSerializer
    queryset = RecurrentPayment.objects.all()


recurrent_payment_detail_api_view = RecurrentPaymentDetailAPIView.as_view()
