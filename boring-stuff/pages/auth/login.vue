<script lang="ts" setup>
import { ref } from 'vue';
//import { useAuthStore } from '@/stores/auth'; // Assuming you have an auth store set up with Pinia
//import { useLoginComposable } from '@/composables/useLogin'; // We'll create this composable

// Composable for login logic
//const { username, password, login, errorMessage } = useLoginComposable();

// Pinia store
//const authStore = useAuthStore();

</script>

<template>
  <div class="container mx-auto p-4">
    <div class="flex flex-col items-center">
      <h2 class="text-lg font-bold mb-4">Login</h2>
      <form @submit.prevent="login" class="w-full max-w-xs">
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium text-gray-700">Username:</label>
          <input type="text" v-model="username" id="username" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
        </div>
        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">Password:</label>
          <input type="password" v-model="password" id="password" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
        </div>
        <div class="flex items-center justify-between">
          <button type="submit" class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Login</button>
        </div>
        <p v-if="errorMessage" class="mt-2 text-sm text-red-600">{{ errorMessage }}</p>
      </form>
    </div>
  </div>
</template>

<style scoped>
/* Add any additional styles here */
</style>
