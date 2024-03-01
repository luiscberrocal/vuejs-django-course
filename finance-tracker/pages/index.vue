<script setup>

import {viewOptions} from "~/constants";

const selectedView = ref(viewOptions[1]);
const isLoading = ref(false);
const transactions = ref([])

const income = computed(() => transactions.value.filter(transaction => transaction.type === 'Income'));
const expense = computed(() => transactions.value.filter(transaction => transaction.type === 'Expense'));

const incomeCount = computed(() => income.value.length);
const expenseCount = computed(() => expense.value.length);

const incomeTotal = computed(() => income.value.reduce((sum, transaction) => sum + transaction.amount, 0));
const expenseTotal = computed(() => expense.value.reduce((sum, transaction) => sum + transaction.amount, 0));

const supabase = useSupabaseClient();

const fetchTransactions = async () => {
  isLoading.value = true;
  try {
    const {data} = await useAsyncData('transactions',
        async () => {
          const {data, error} = await supabase.from('transactions').select('*');
          return data;
          if (error) {
            return []
            //throw error;
          }
          return data
        });
    return data.value;
  } finally {
    isLoading.value = false;
  }
}

const refreshTransactions = async () => transactions.value = await fetchTransactions();

await refreshTransactions()

const transactionsGroupedByDate = computed(() => {
  let grouped = {}
  for (const transaction of transactions.value) {
    const date = new Date(transaction.created_at).toISOString().split('T')[0]
    if (!grouped[date]) {
      grouped[date] = []
    }
    grouped[date].push(transaction)
  }
  return grouped
})
console.log(transactionsGroupedByDate.value)
</script>

<template>
  <section class="flex items-center justify-between mb-10">
    <h1 class="text-4xl font-extrabold">Summary</h1>
    <div>
      <USelectMenu :options="viewOptions" v-model="selectedView"/>
    </div>
  </section>
  <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 sm:gap-16 mb-10">
    <Trend title="Income" color="green" :amount="incomeTotal" last-amount="5000" :loading="isLoading"/>
    <Trend title="Expense" color="red" :amount="expenseTotal" last-amount="3000" :loading="isLoading"/>
    <Trend title="Investments" color="green" :amount="3000" last-amount="2000" :loading="isLoading"/>
    <Trend title="Savings" color="red" :amount="3000" last-amount="4000" :loading="isLoading"/>
  </section>

  <section v-if="!isLoading">
    <div v-for="(transactionsOnDay, date) in transactionsGroupedByDate" :key="date" class="mb-10">
      <DailyTransactionSummary :date="date" :transactions="transactionsOnDay"/>
      <Transaction v-for="transaction in transactionsOnDay" :key="transaction.id"
                   :transaction="transaction"
                   @deleted="refreshTransactions()"/>
    </div>
  </section>
  <section v-else>
    <USkeleton class="w-full h-8 mb-2" v-for="i in 4" :key="i"/>
  </section>
</template>

<style scoped>

</style>
