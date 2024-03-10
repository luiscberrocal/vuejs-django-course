<script lang="ts" setup>
const url = 'http://127.0.0.1:8000/api/payments/recurrent-payments/'
console.log(url)
const {data: recurrentPayments, error, status} = await useFetch(url);
const paymentToCreate = null;

const urlPayments = 'http://127.0.0.1:8000/api/payments/payments/?limit=4';
const {data: payments, error: errorPayments, status: statusPayments} = await useFetch(urlPayments);

</script>

<template>
  <div class="container place-content-center">
    <h1>Boring stuff</h1>
    <p>Some boring stuff</p>
    <div class="grid grid-cols-2 gap-2">
      <div>
        <header class="bs-header">
          Recurrent Payments
        </header>
        <div v-if="error">
          <p>error: {{ error }}</p>
          <p>status: {{ status }}</p>
        </div>
        <DebugBlock level="info">
          <template #title>Recurrent Payments</template>
          recurrentPayments: {{ recurrentPayments }}
        </DebugBlock>
      </div>

      <div>
        <header class="bs-header">
          Payments
        </header>
        <div v-if="paymentToCreate">
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>

</style>
