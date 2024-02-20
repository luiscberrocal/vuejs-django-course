<script lang="ts" setup>
const now = new Date().toISOString();
</script>

<template>
  <h2>Make Payment</h2>
  <div>
    <form action="">
      <div class="form-group">
        <label for="date">Date:</label>
        <input type="text" id="date" class="form-control" :value="now">
      </div>
      <div class="form-group mt-3">
        <label for="amount">Amount:</label>
        <input type="number" id="amount" class="form-control">
      </div>
    </form>
  </div>
</template>

<style scoped>

</style>
