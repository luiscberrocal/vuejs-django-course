<script lang="ts" setup>

import {viewOptions} from "~/constants";

const selectedView = ref(viewOptions[1]);
const supabase = useSupabaseClient();

const {data, error} = await supabase.from('transactions').select('*');
console.log('data', data, 'error', error);

const transactions = ref([])

transactions.value = data;


</script>

<template>
  <section class="flex items-center justify-between mb-10">
    <h1 class="text-4xl font-extrabold">Summary</h1>
    <div>
      <USelectMenu :options="viewOptions" v-model="selectedView"/>
    </div>
  </section>
  <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 sm:gap-16 mb-10">
    <Trend title="Income" color="green" :amount="3000" last-amount="5000" :loading="false"/>
    <Trend title="Expense" color="red" :amount="3000" last-amount="3000" :loading="false"/>
    <Trend title="Investments" color="green" :amount="3000" last-amount="2000" :loading="false"/>
    <Trend title="Savings" color="red" :amount="3000" last-amount="4000" :loading="false"/>
  </section>

  <section>
      <Transaction v-for="transaction in transactions" :key="transaction.id" :transaction="transaction"></Transaction>
  </section>
</template>

<style scoped>

</style>
