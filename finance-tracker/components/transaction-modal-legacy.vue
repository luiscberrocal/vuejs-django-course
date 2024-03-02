<script setup>
import {categories, transactionTypes} from "~/constants";
import {z} from "zod";

const props = defineProps({
  modelValue: Boolean
})

const emit = defineEmits(['update:modelValue', 'saved']);
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
  // type: z.enum(transactionTypes),`
  amount: z.number().positive('Amount need to be positive'),
  created_at: z.string(),
  description: z.string().optional(),
  // category: z.enum(categories)
})
const incomeSchema = z.object({
  type: z.literal('Income')
})
const investmentSchema = z.object({
  type: z.literal('Investment')
})
const savingsSchema = z.object({
  type: z.literal('Savings')
})
const expenseSchema = z.object({
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
const form = ref();
const isLoading = ref(false);

const supabase = useSupabaseClient();
const toast = useToast();

const save = async () => {
  console.log('>>>>>>>>>>>>>>>>>>>>>')
  if (form.value.errors.length) return
  isLoading.value = true;
  try {
    console.log('Saving transaction', state.value)
    const {error} = await supabase.from('transactions')
        .upsert({...state.value});
    // error = null;
    //if (error) {
    //  throw error;
    //}
    if (!error) {
      toast.add({
        title: 'Transaction added',
        icon: 'i-heroicons-check-circle',
        color: 'green'
      })
      isOpen.value = false;
      emit('saved');
    } else {
      console.log('Error while adding transaction', error)
    }
  } catch (error) {
    toast.add({
      title: 'Error while adding transaction',
      description: error.message,
      icon: 'i-heroicons-exclamation-circle',
      color: 'red'
    })
    console.error(error)

  } finally {
    isLoading.value = false;
  }
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
        <UButton type="submit" color="black" variant="solid" :loading="isLoading">Save</UButton>
      </UForm>
    </UCard>
  </UModal>

</template>

<style scoped>

</style>
