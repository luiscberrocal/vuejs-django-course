<script setup>
const {id} = useRoute().params;
const uri = `https://fakestoreapi.com/products/${id}`;
const {data: product} = await useFetch(uri, {key: id});
if (!product.value) {
  throw createError({statusCode: 404, statusMessage: 'Product not found'});
}
definePageMeta({
  layout: "products",
});
</script>

<template>
  <head>
    <Title>Nuxt Dojo | {{ product.title }}</Title>
    <Meta name="description" :content="product.description"></Meta>
  </head>
  <ProductDetails :product="product"></ProductDetails>
</template>

<style scoped>

</style>
