<script lang="ts" setup>
const props = defineProps(
    {
      transaction: Object
    }
)
const {currency} = useCurrency(props.transaction.amount);
const isLoading = ref(false);

const supabase = useSupabaseClient();
const toast = useToast();
const deleteTransaction = async () => {
  isLoading.value = true;
  try {
    await supabase.from('transactions').delete().eq('id', props.transaction.id);
    toast.add({
      title: 'Transaction deleted',
      icon: 'i-heroicons-check-circle',
      color: 'green'
    })
  } catch (error) {
    toast.add({
      title: 'Error while deleting transaction',
      icon: 'i-heroicons-exclamation-circle',
      color: 'red'
    })
  } finally {
    isLoading.value = false;
  }
}
const items = [
  [
    {
      label: 'Edit',
      icon: 'i-heroicons-pencil-square-20-solid',
      click: () => {
        console.log('Edit');
      }
    },
    {
      label: 'Delete',
      icon: 'i-heroicons-trash-20-solid',
      click: deleteTransaction
    }
  ]
]
const isIncome = computed(() => {
  return props.transaction.type === 'Income'
})

const icon = computed(() => {
  return isIncome.value ? 'i-heroicons-arrow-up-right' : 'i-heroicons-arrow-down-left'
});

const iconColor = computed(() => {
  return isIncome.value ? 'green' : 'red'
});

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
          <UButton color="white" variant="ghost" trailing-icon="i-heroicons-ellipsis-horizontal" :loading="isLoading"/>
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
