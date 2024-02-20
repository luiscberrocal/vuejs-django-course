<script lang="ts" setup>
const {recurrentPayments} = defineProps(['recurrentPayments']);
</script>

<template>
  <ul>
    <li v-for="payment in recurrentPayments" :key="payment.id">
      <div class="flex card justify-between">
        <h3 class="text-xl font-bold">{{ payment.name }}</h3>
        <div>
          <button class="btn">Edit</button>
        </div>
      </div>
      <p>{{ payment.amount }}</p>
    </li>
  </ul>
</template>

<style scoped>

</style>
