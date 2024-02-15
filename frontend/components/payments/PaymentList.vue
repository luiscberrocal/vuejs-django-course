<script>
import RecurrentPaymentItem from './RecurrentPaymentItem.vue';

export default {
  components: {RecurrentPaymentItem},
  props: [],
  data() {
    return {
      recurrentPayments: []
    };
  },
  methods: {
    loadPayments() {
      const url = 'http://127.0.0.1:8000/api/payments/recurrent-payments/'
      fetch(url)
          .then(response => response.json())
          .then(data => {
            console.log(data);
            const payments = data.map(payment => {
              return {
                id: payment.id,
                name: payment.name,
                amount: payment.amount,
                dateDue: payment.date_due,
              };
            });
            this.recurrentPayments = payments;
          });
    }
  },
  computed: {}
}
</script>

<template>
  <div>
    <h2>Payments</h2>
    <button @click="loadPayments">Load Payments</button>
    <ul>
      <recurrent-payment-item
          v-for="payment in recurrentPayments"
          :key="payment.id"
          :recurrent-payment="payment"></recurrent-payment-item>
    </ul>
  </div>
</template>

<style scoped>

div {
  list-style: none;
  margin: 2rem auto;
  max-width: 40rem;
  padding: 0;
}

ul {
  list-style: none;
  margin: 2rem auto;
  max-width: 40rem;
  padding: 0;
}
</style>
