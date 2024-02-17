<script setup>
const {id} = useRoute().params;
definePageMeta({
  layout: "products",
});
</script>

<template>
  <h2>Product {{ id }} </h2>
  <p>Product description</p>
</template>

<style scoped>

</style>
