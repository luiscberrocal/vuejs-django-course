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
const trendingUp = computed(() => {
  return props.todaysCount >= props.average
})
const icon = computed(() => {
  return trendingUp.value ? 'i-heroicons-arrow-trending-up' : 'i-heroicons-arrow-trending-down'
})
</script>

<template>
  <div class="m-2 p-1">
    <div class="font-bold" :class="{'green': trendingUp, 'red': !trendingUp}">{{ name }}</div>
    <p>Average: {{ average }}</p>
    <p>Today's Count: {{ todaysCount }}</p>
    <div class="flex space-x-1">
      <UIcon :name="icon" class="w-6 h-6" :class="{'green': trendingUp, 'red': !trendingUp}"/>
      <div class="text-gray-500 dark:text-gray-400">
        52% to average.
      </div>
    </div>
  </div>
</template>

<style scoped>
.green {
  @apply text-green-600 dark:text-green-400;
}

.red {
  @apply text-red-600 dark:text-red-400;
}
</style>
