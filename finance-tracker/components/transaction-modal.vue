<script lang="ts" setup>
import {categories, transactionTypes} from "~/constants";

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
      <UFormGroup label="Transaction type" name="type" :required="true" class="mb-4">
        <USelect placeholder="Transaction type" :options="transactionTypes"></USelect>
      </UFormGroup>
      <UFormGroup label="Amount" name="amount" :required="true" class="mb-4">
        <UInput type="number" placeholder="Enter amount"/>
      </UFormGroup>
      <UFormGroup label="Transaction date" name="created_at" :required="true" class="mb-4">
        <UInput type="date" placeholder="Date" icon="i-heroicons-calendar-days-20-solid"/>
      </UFormGroup>
      <UFormGroup label="Description" name="description" :required="false" class="mb-4">
        <UInput type="text" placeholder="Transaction description"/>
      </UFormGroup>
      <UFormGroup label="Category" name="category" :required="true" class="mb-4">
        <USelect placeholder="Categories" :options="categories"></USelect>
      </UFormGroup>
      <UButton type="submit" color="black" variant="solid">Save</UButton>
    </UCard>
  </UModal>

</template>

<style scoped>

</style>
