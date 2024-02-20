<script lang="ts" setup>
const {recurrentPayments} = defineProps(['recurrentPayments']);
</script>

<template>
  <ul>
    <li v-for="payment in recurrentPayments" :key="payment.id">
      <div class="card m-3">
        <div class="flex justify-between">
          <h3 class="text-xl font-bold">{{ payment.name }}</h3>
          <div>
            <button class="btn mx-0.5">Pay</button>
            <button class="btn mx-0.5">Edit</button>
          </div>
        </div>
        <div>
          <p>Amount: ${{ payment.amount }} <span v-if="payment.is_amount_fixed">(Fixed)</span></p>
          <p>Date due: {{ payment.date_due }}</p>
          <p>Is Active: {{ payment.is_active }}</p>
        </div>
      </div>
    </li>
  </ul>
</template>

<style scoped>

</style>
