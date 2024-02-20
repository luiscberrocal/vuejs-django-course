<script lang="ts" setup>
const url = 'http://127.0.0.1:8000/api/payments/recurrent-payments/'
console.log(url)
const {data: recurrentPayments, error, status} = await useFetch(url);
const paymentToCreate = null;

</script>

<template>
  <div class="container place-content-center">
    <h1>Boring stuff</h1>
    <p>Some boring stuff</p>
    <div class="grid grid-cols-2 gap-2">
      <div>
        <header class="bg-gray-500 text-white p-4 rounded-lg">
          Recurrent Payments
        </header>
        <div v-if="error">
          <p>error: {{ error }}</p>
          <p>status: {{ status }}</p>
        </div>
        <PaymentsList :recurrentPayments="recurrentPayments"></PaymentsList>
      </div>
      <div>
        <header class="bg-gray-500 text-white p-4 rounded-lg">
          Payments
        </header>
        <div v-if="paymentToCreate">
          <PaymentsMakePayment></PaymentsMakePayment>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>

</style>
