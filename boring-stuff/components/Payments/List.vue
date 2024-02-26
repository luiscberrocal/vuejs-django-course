<script setup lang="ts">
defineProps(['paymentsData']);
</script>

<template>
  <div>
    <div>
      count {{ paymentsData.count }}
    </div>
    <div v-for="payment in paymentsData.results" :key="payment.id">
      <div class="card m-3">
        <div class="flex justify-between">
          <h3 class="text-xl font-bold">{{ payment.recurrent_payment_name }}</h3>
          <div class="flex">
            <button class="btn flex mx-0.5">
              <span class="material-symbols-outlined">edit</span>
              <span>Edit</span>
            </button>
            <button class="btn flex mx-0.5">
              <span class="h-5 material-symbols-outlined">delete</span>
              <span>Delete</span>
            </button>
          </div>
        </div>
        <div>
          <p>Amount: ${{ payment.amount }}</p>
          <p>Date: {{ payment.date }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
