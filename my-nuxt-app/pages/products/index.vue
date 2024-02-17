<script lang="ts" setup>
definePageMeta({
  layout: "products",
});
const {data: products} = await useFetch('https://fakestoreapi.com/products')
</script>

<template>
  <h1>Products</h1>
  <div class="grid grid-cols-4 gap-5">
    <div v-for="p in products">
      <ProductCard :product="p" :key="p.id"/>

    </div>
  </div>
</template>


<style scoped>
.router-link-exact-active {
  color: red;
}
</style>
