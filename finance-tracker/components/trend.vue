<script lang="ts" setup>
const props = defineProps(
    {
      title: String,
      amount: Number,
      lastAmount: Number,
      color: {
        type: String
      },
      loading: {
        type: Boolean,
        default: false
      }
    }
)
const trendingUp = computed(() => {
  return props.amount >= props.lastAmount
})

const icon = computed(() => {
  return trendingUp.value ? 'i-heroicons-arrow-trending-up' : 'i-heroicons-arrow-trending-down'
})
</script>

<template>
  <div>
    <div class="font-bold" :class="{'green': trendingUp, 'red': !trendingUp}">{{ title }}</div>
    <div class="text-2xl font-extrabold text-black dark:text-white mb-2">
      <USkeleton v-if="loading" class="w-full h-8"/>
      <div v-else>
        {{ amount }}
      </div>
    </div>
    <div>
      <USkeleton v-if="loading" class="w-full h-6"/>
      <div v-else class="flex space-x-1 items-center text-sm">
        <UIcon :name="icon" class="w-6 h-6" :class="{'green': trendingUp, 'red': !trendingUp}"/>
        <div class="text-gray-500 dark:text-gray-400">
          30% up from last month.
        </div>
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
