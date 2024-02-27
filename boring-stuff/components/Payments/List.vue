<script setup lang="ts">
defineProps(['paymentsData']);
</script>

<template>
  <div>
    <div class="container mx-auto p-4 flex justify-between">
      <button class="btn w-32">Previous</button>
      <button class="btn w-32">Next</button>
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
          <p>Date: {{ payment.date }} <span>{{ payment.age }}</span></p>
        </div>
      </div>
    </div>
      <debug-block>{{ paymentsData}}</debug-block>
  </div>
</template>

<style scoped>

</style>
