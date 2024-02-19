<script lang="ts" setup>
const url = 'http://127.0.0.1:8000/api/payments/recurrent-payments/'
console.log(url)
const {data: recurrentPayments} = await useFetch(url)
//const recurrentPayments = await useFetch(url); //.catch(err => console.log(err));
console.log(recurrentPayments)
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
        <p>Payment: {{ recurrentPayments }}</p>
        <ul>

          <li v-for="payment in recurrentPayments" :key="payment.id">
            <p>{{ payment.name }}</p>
            <p>{{ payment.amount }}</p>
          </li>
        </ul>
      </div>
      <div>
        <header class="bg-gray-500 text-white">
          Payments
        </header>
      </div>

    </div>
  </div>
</template>

<style scoped>

</style>
