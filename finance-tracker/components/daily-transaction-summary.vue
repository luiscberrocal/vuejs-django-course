<script lang="ts" setup>
const props = defineProps(
    {
      date: String,
      transactions: Array
    }
)
const {currency} = useCurrency(props.transaction.amount);
</script>

<template>
  <div class="grid grid-cols-2 py-4 border-b border-gray-200 dark:border-gray-800 text-gray-900 dark:text-gray-100">
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-1">
        <UIcon :name="icon" :class="[iconColor]"></UIcon>
        <div>{{ transaction.description }}</div>
      </div>
      <div>
        <UBadge color="white" v-if="transaction.category">{{ transaction.category }}</UBadge>
      </div>
    </div>
    <div class="flex items-center justify-end space-x-2">
      <div>{{ currency }}</div>
      <div>
        <UDropdown :items="items" :popper="{placement: 'bottom-start'}">
          <UButton color="white" variant="ghost" trailing-icon="i-heroicons-ellipsis-horizontal"/>
        </UDropdown>
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
