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
const percentageTrend = computed(() => {
  if (props.lastAmount === 0 || props.amount === 0) {
    return '⚓%'
  }
  const bigger = Math.max(props.amount, props.lastAmount);
  const smaller = Math.min(props.amount, props.lastAmount);
  const ratio = ((bigger - smaller) / smaller) * 100;
  console.log('ratio', Math.ceil(ratio), 'big', bigger, 'small', smaller);
  return `${Math.ceil(ratio)}%`
})

const {currency} = useCurrency(props.amount);

</script>

<template>
  <div>
    <div class="font-bold" :class="{'green': trendingUp, 'red': !trendingUp}">{{ title }}</div>
    <div class="text-2xl font-extrabold text-black dark:text-white mb-2">
      <USkeleton v-if="loading" class="w-full h-8"/>
      <div v-else>
        {{ currency }}
      </div>
    </div>
    <div>
      <USkeleton v-if="loading" class="w-full h-6"/>
      <div v-else class="flex space-x-1 items-center text-sm">
        <UIcon :name="icon" class="w-6 h-6" :class="{'green': trendingUp, 'red': !trendingUp}"/>
        <div class="text-gray-500 dark:text-gray-400">
          {{ percentageTrend }} vs last period.
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
