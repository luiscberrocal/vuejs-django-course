<script>
export default {
  props: ['recurrentPayment'],
  data() {
    return {};
  },
  methods: {},
  computed: {}
}
</script>

<template>
  <li>
    <h3>{{ recurrentPayment.name }}</h3>
    <p><span class="title">Amount:</span> {{ recurrentPayment.amount }}</p>
    <p><span class="title">Date:</span> {{ recurrentPayment.dateDue }}</p>
  </li>
</template>

<style scoped>
p span.title {
  font-weight: bold;
  margin: 0;
  padding: 0;
  margin-bottom: 0.5rem;
  max-width: 10rem;
}
</style>
