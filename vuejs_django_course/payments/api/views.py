import logging

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from vuejs_django_course.payments.api.serializers import RecurrentPaymentSerializer, PaymentSerializer
from vuejs_django_course.payments.models import RecurrentPayment

logger = logging.getLogger(__name__)


class RecurrentPaymentListAPIView(ListAPIView):
    serializer_class = RecurrentPaymentSerializer
    queryset = RecurrentPayment.objects.all()


recurrent_payment_list_api_view = RecurrentPaymentListAPIView.as_view()


class RecurrentPaymentDetailAPIView(RetrieveAPIView):
    serializer_class = RecurrentPaymentSerializer
    queryset = RecurrentPayment.objects.all()


recurrent_payment_detail_api_view = RecurrentPaymentDetailAPIView.as_view()


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer

    def post(self, request, *args, **kwargs):
        logger.warning(f'>>> PaymentCreateAPIView.post - data: {request.data}')
        return super().post(request, *args, **kwargs)


payment_create_api_view = PaymentCreateAPIView.as_view()
