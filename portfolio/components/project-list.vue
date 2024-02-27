<script lang="ts" setup>

let projectUrl = 'https://api.github.com/users/luiscberrocal/repos';
const {error, pending, data} = await useFetch(projectUrl);

</script>

<template>
  <div>
    <section v-if="pending">Loading...</section>
    <section v-else-if="error">Error: {{ error.message }}</section>
    <section v-else>{{ data}}</section>

  </div>

</template>

<style scoped>

</style>
