<script lang="ts" setup>
const route = useRoute();

console.log(route)

</script>


<template>
  <div>
    <h2>In a post {{ route.params.slug}}</h2>
  </div>
</template>

<style scoped>

</style>
