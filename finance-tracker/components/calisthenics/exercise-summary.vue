<script lang="ts" setup>
const props = defineProps(
    {
      name: {
        type: String,
        required: true
      },
      average: {
        type: Number,
        required: true
      },
      todaysCount: {
        type: Number,
        required: true
      }
    }
)
</script>

<template>
  <div>
    <h1>{{ name }} Summary</h1>
    <p>Average: {{ average }}</p>
    <p>Today's Count: {{ todaysCount }}</p>
  </div>
</template>

<style scoped>

</style>
