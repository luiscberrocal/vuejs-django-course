from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from vuejs_django_course.payments.models import Payment
from vuejs_django_course.payments.tests.factories import RecurrentPaymentFactory


class TestPaymentCreateAPIView(APITestCase):

    def test_create(self):
        recurrent_payment = RecurrentPaymentFactory.create()
        data = {
            'recurrent_payment': recurrent_payment.id,
            'date': '2019-01-01 13:13:13',
            'amount': 100
        }
        url = reverse('payments:payment-create')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Payment.objects.count(), 1)
