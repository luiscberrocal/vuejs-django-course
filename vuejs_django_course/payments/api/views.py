import logging

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from vuejs_django_course.core.pagination import StandardResultsSetPagination
from vuejs_django_course.payments.api.serializers import RecurrentPaymentSerializer, PaymentSerializer
from vuejs_django_course.payments.filters import PaymentFilter
from vuejs_django_course.payments.models import RecurrentPayment, Payment

logger = logging.getLogger(__name__)


class RecurrentPaymentListAPIView(ListAPIView):
    serializer_class = RecurrentPaymentSerializer
    queryset = RecurrentPayment.objects.all()


recurrent_payment_list_api_view = RecurrentPaymentListAPIView.as_view()


class RecurrentPaymentDetailAPIView(RetrieveAPIView):
    serializer_class = RecurrentPaymentSerializer
    queryset = RecurrentPayment.objects.all()


recurrent_payment_detail_api_view = RecurrentPaymentDetailAPIView.as_view()


class RecurrentPaymentCreateAPIView(CreateAPIView):
    serializer_class = RecurrentPaymentSerializer


recurrent_payment_create_api_view = RecurrentPaymentCreateAPIView.as_view()


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer

    def post(self, request, *args, **kwargs):
        logger.warning(f'>>> PaymentCreateAPIView.post - data: {request.data}')
        serializer = self.get_serializer(data=request.data)
        is_valid = serializer.is_valid()
        if not is_valid:
            logger.error(f'>>> PaymentCreateAPIView.post - errors: {serializer.errors}')
        return super().post(request, *args, **kwargs)


payment_create_api_view = PaymentCreateAPIView.as_view()


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all().order_by('-date')
    pagination_class = StandardResultsSetPagination
    # filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter


payment_list_api_view = PaymentListAPIView.as_view()
