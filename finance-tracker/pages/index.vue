<script lang="ts" setup>
const viewOptions = ['Yearly', 'Monthly', 'Weekly', 'Daily'];
const selectedView = ref(viewOptions[1]);

</script>

<template>
  <section class="flex items-center justify-between mb-10">
    <h1 class="text-4xl font-extrabold">Summary</h1>
    <div>
      <USelectMenu :options="viewOptions" v-model="selectedView"/>
    </div>

  </section>
</template>

<style scoped>

</style>
