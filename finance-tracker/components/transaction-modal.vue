<script lang="ts" setup>
import {categories, transactionTypes} from "~/constants";
import {z} from "zod";

const props = defineProps({
  modelValue: Boolean
})

const emit = defineEmits(['update:modelValue']);
const isOpen = computed(
    {
      get: () => props.modelValue,
      set: (value) => {
        if (!value) resetForm();
        emit('update:modelValue', value);
      }
    }
)
const defaultSchema = z.object({
  // type: z.enum(transactionTypes),
  amount: z.number().positive('Amount need to be positive'),
  created_at: z.string(),
  description: z.string().optional(),
  // category: z.enum(categories)
})
const incomeSchema = defaultSchema.extend({
  type: z.literal('Income')
})
const investmentSchema = defaultSchema.extend({
  type: z.literal('Investment')
})
const savingsSchema = defaultSchema.extend({
  type: z.literal('Savings')
})
const expenseSchema = defaultSchema.extend({
  type: z.literal('Expense'),
  category: z.enum(categories)
})
const schema = z.intersection(
    z.discriminatedUnion('type', [incomeSchema, expenseSchema, investmentSchema, savingsSchema]),
    defaultSchema
)

const initialState = {
  type: 'Expense',
  amount: 0,
  created_at: new Date().toISOString().split('T')[0],
  description: undefined,
  category: undefined
}
const state = ref({
      ...initialState
    }
)
const resetForm = () => {
  Object.assign(state.value, initialState);
  //form.value.errors.clear();
}
const form = ref(null)

const save = async () => {
  if (form.value.errors.length > 0) {
    return
  }
  // if (form.value.validate()) {
  //   console.log('Valid')
  // } else {
  //   console.log('Invalid')
  // }
}

</script>

<template>
  <UModal v-model="isOpen">
    <UCard>
      <template #header>
        Add Transaction
      </template>
      <UForm :state="state" :schema="schema" :ref="form" @submit.prevent="save">
        <UFormGroup label="Transaction type" name="type" :required="true" class="mb-4">
          <USelect placeholder="Transaction type" :options="transactionTypes" v-model="state.type"></USelect>
        </UFormGroup>
        <UFormGroup label="Amount" name="amount" :required="true" class="mb-4">
          <UInput type="number" placeholder="Enter amount" v-model.number="state.amount"/>
        </UFormGroup>
        <UFormGroup label="Transaction date" name="created_at" :required="true" class="mb-4">
          <UInput type="date" placeholder="Date" icon="i-heroicons-calendar-days-20-solid" v-model="state.created_at"/>
        </UFormGroup>
        <UFormGroup label="Description" name="description" :required="false" class="mb-4">
          <UInput type="text" placeholder="Transaction description" v-model="state.description"/>
        </UFormGroup>
        <UFormGroup label="Category" name="category" :required="true" class="mb-4" v-if="state.type=='Expense'">
          <USelect placeholder="Categories" :options="categories" v-model="state.category"></USelect>
        </UFormGroup>
        <UButton type="submit" color="black" variant="solid">Save</UButton>
      </UForm>
    </UCard>
  </UModal>

</template>

<style scoped>

</style>
