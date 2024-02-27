from django.urls import path

from vuejs_django_course.payments.api.views import recurrent_payment_list_api_view, recurrent_payment_detail_api_view, \
    payment_create_api_view, payment_list_api_view, recurrent_payment_create_api_view

app_name = 'payments'

urlpatterns = [
    path('recurrent-payments/', recurrent_payment_list_api_view, name='recurrent-payment-list'),
    path('recurrent-payments/create/', recurrent_payment_create_api_view, name='recurrent-payment-create'),
    path('recurrent-payments/<int:pk>/', recurrent_payment_detail_api_view, name='recurrent-payment-detail'),
    path('payments/create/', payment_create_api_view, name='payment-create'),
    path('payments/', payment_list_api_view, name='payment-list'),
]
