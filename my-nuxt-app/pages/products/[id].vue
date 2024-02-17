<script setup>
const {id} = useRoute().params;
const uri = `https://fakestoreapi.com/products/${id}`;
const {data: product} = await useFetch(uri, {key: id});

definePageMeta({
  layout: "products",
});
</script>

<template>
  <p>{{ product.title }}</p>
  <p>{{ product.price }}</p>
  <p>{{ product.id }}</p>
</template>

<style scoped>

</style>
