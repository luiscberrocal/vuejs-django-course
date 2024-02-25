<script lang="ts" setup>
const {recurrentPayments} = defineProps(['recurrentPayments']);
const makePayment = (id) => {
  navigateTo('/payments/pay/'+ id);
}
</script>/

<template>
  <ul>
    <li v-for="payment in recurrentPayments" :key="payment.id">
      <div class="card m-3">
        <div class="flex justify-between">
          <h3 class="text-xl font-bold">{{ payment.name }}</h3>
          <div class="flex">
            <button class="btn flex mx-0.5" @click="makePayment(payment.id)">
              <span class="material-symbols-outlined">payments</span>
              <span>Pay</span>
            </button>
            <button class="btn flex mx-0.5">
              <span class="material-symbols-outlined">edit</span>
              <span>Edit</span>
            </button>
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
