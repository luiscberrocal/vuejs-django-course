<script setup lang="ts">
const paymentsData = defineProps(['paymentsData']);
</script>

<template>
  <div>
      <div>
          count {{ paymentsData.count }}
      </div>
      <div v-for="payment for paymentsData.results" :key="payment.id">
      <div class="card m-3">
          <div class="flex justify-between">
              <h3 class="text-xl font-bold">{{ payment.name }}</h3>
              <div class="flex">
                  <button class="btn flex mx-0.5">
                      <span class="material-symbols-outlined">payments</span>
                      <span>Pay</span>
                  </button>
              </div>
          </div>
          <div>
              <p>Amount: ${{ payment.amount }}</p>
          </div>
      </div>
      </div>
      <div>{{ paymentsData}}</div>
  </div>
</template>

<style scoped>

</style>
