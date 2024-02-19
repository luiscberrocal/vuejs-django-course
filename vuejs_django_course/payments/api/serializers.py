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


class PaymentSerializer(serializers.Serializer):
    recurrent_payment = RecurrentPayment()

    class Meta:
        model = Payment
        fields = ('id', 'recurrent_payment', 'date', 'amount')
