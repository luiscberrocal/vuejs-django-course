<script lang="ts" setup>
const props = defineProps({
  modelValue: Boolean
})

const emit = defineEmits(['update:modelValue']);
const isOpen = computed(
    {
      get: () => props.modelValue,
      set: (value) => emit('update:modelValue', value)
    }
)
</script>

<template>
  <UModal v-model="isOpen">
    <UCard>
      <template #header>
        Add Transaction
      </template>

      <div>Hello!</div>
    </UCard>
  </UModal>

</template>

<style scoped>

</style>
