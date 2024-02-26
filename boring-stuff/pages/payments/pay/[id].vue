<script lang="ts" setup>

const getNow = () => {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0'); // Months are zero-indexed
  const day = String(now.getDate()).padStart(2, '0');
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');

  const formattedDate = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
  console.log(formattedDate); // This will print the date in "YYYY-MM-DD HH:MM:SS" format
  return formattedDate;
}

const now = ref(getNow());

const {id} = useRoute().params;

const url = `http://127.0.0.1:8000/api/payments/recurrent-payments/${id}/`
const {data: recurrentPayment, error, status} = await useFetch(url);
const errorMessage = ref('');

const postPayment = async () => {
  try {

    console.log('recurrentPayment', recurrentPayment.value)
    const url = 'http://127.0.0.1:8000/api/payments/payments/create/'
    const payload = {
      recurrent_payment: recurrentPayment.value.id,
      date: now.value,
      amount: recurrentPayment.value.amount
    }
    console.log('payload', payload);
    //  const url = `http://`
    const response = await $fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });
    console.log('response', response);
  } catch (error) {
    console.error('error', error);
    errorMessage.value = error.message;
  }
};

</script>

<template>
  <h2>Make Payment for {{ recurrentPayment.name }}</h2>
  <div>
    <form @submit.prevent="postPayment">
      <div class="form-group">
        <label for="date">Date:</label>
        <input type="text" id="date" class="text-input" v-model="now">
      </div>
      <div class="form-group mt-3">
        <label for="amount">Amount:</label>
        <input type="text" id="amount" class="text-input" v-model="recurrentPayment.amount">
      </div>
      <button class="btn" type="submit">Save</button>
    </form>
    <p v-if="errorMessage" class="mt-2 text-sm text-red-600">{{ errorMessage }}</p>
  </div>
</template>

<style scoped>

</style>
