<script>
export default {
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
      <li v-for="payment in recurrentPayments" :key="payment.id">
        {{ payment.name }} - {{ payment.amount }} - {{ payment.dateDue }}
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>
