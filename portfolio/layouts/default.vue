<script lang="ts" setup>

</script>

<template>
  <div class="container mx-auto max-w-2xl mt-5">
    <header class="flex justify-between items-center">
      <NuxtLink to="/" class="text-xl">Luis C. Berrocal</NuxtLink>
      <nav class="font-mono">
        <ul class="flex space-x-4">
          <li>
            <NuxtLink to="/">Home</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/about">About</NuxtLink>
          </li>
        </ul>
      </nav>

    </header>

    <main class="p2">
      <slot></slot>
    </main>


  </div>
</template>

<style scoped>

</style>
