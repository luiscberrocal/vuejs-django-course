<script setup>
defineProps(['error'])

const handleClearError = () => {
  clearError({redirect: '/'})
}
</script>

<template>
  <NuxtLayout>
    <div class="mt-7 max-w-sm mx-auto text-center card">
      <p class="mt-7 text-7xl font-bold">{{ error.statusCode }}</p>
      <p class="mt-7 text-6xl">Ooops</p>
      <p class="mt-7">{{ error.message }}</p>
      <button class="btn" @click="handleClearError">Got home</button>
    </div>
  </NuxtLayout>
</template>

<style scoped>

</style>
