from factory import Sequence
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class RecurrentPaymentFactory(DjangoModelFactory):
    class Meta:
        model = 'payments.RecurrentPayment'

    name = Sequence(lambda n: f'Recurrent payment {n}')
    amount = 100
    description = FuzzyText(length=100)
    date_due = faker.date_this_year()
    is_active = True
    is_amount_fixed = True


class PaymentFactory(DjangoModelFactory):
    class Meta:
        model = 'payments.Payment'

    recurrent_payment = SubFactory(RecurrentPaymentFactory)
    date = faker.date_this_year()
    amount = 100
