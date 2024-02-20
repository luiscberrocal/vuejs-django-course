<script lang="ts" setup>
const now = new Date().toISOString();

const {id} = useRoute().params;

const url = `http://127.0.0.1:8000/api/payments/recurrent-payments/${id}/`
const {data: recurrentPayment, error, status} = await useFetch(url);
//let amount = await recurrentPayment.amount;
// console.log('NEW AMOUNT', amount)
const postPayment = async () => {
  console.log(recurrentPayment)
  const url = `http://127.0.0.1:8000/api/payments/payments/create/`
  //  const url = `http://`
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      recurrent_payment: recurrentPayment.id,
      date: '2024-02-20', //now,
      amount: recurrentPayment.amount
    })
  });
  console.log('response', response);
};

</script>

<template>
  <h2>Make Payment for {{ recurrentPayment.name }}</h2>
  <div>
    <form @submit.prevent="postPayment">
      <div class="form-group">
        <label for="date">Date:</label>
        <input type="text" id="date" class="form-control" v-model="now">
      </div>
      <div class="form-group mt-3">
        <label for="amount">Amount:</label>
        <input type="text" id="amount" class="form-control" v-model="recurrentPayment.amount">
      </div>
      <button type="submit">Save</button>
    </form>
  </div>
</template>

<style scoped>

</style>
