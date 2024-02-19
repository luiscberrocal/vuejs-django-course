<script lang="ts" setup>
const {data} = await useFetch('/api/currency/MXN')
// const {data} = await useFetch('/api/ninja');
</script>

<template>
  <div>
    <h2>About</h2>
    <p>My application</p>
    <p>Data: {{ data }}</p>
  </div>
</template>
<style scoped>

</style>
