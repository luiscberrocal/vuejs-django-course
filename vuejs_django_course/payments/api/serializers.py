from rest_framework import serializers

from vuejs_django_course.payments.models import RecurrentPayment, Payment


class RecurrentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurrentPayment
        fields = ('id', 'name', 'amount', 'description', 'date_due', 'is_active', 'is_amount_fixed')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.user != user:
            raise serializers.ValidationError('You are not allowed to update this recurrent payment')
        return super().update(instance, validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    # recurrent_payment = RecurrentPaymentSerializer()
    recurrent_payment_name = serializers.CharField(source='recurrent_payment.name', read_only=True)

    class Meta:
        model = Payment
        fields = ('id', 'recurrent_payment', 'recurrent_payment_name', 'date', 'amount')

    def create(self, validated_data):
        # user = self.context['request'].user
        # validated_data['created_by'] = user
        payment = Payment.objects.create(**validated_data)
        return payment
