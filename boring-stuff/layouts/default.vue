<script lang="ts">
</script>

<template>
  <div>
    <header class="shadow-sm bg-white">
      <nav class="container mx-auto p-4 flex justify-between">
        <NuxtLink to="/" class="font-bold">The Boring Stuff</NuxtLink>
        <ul class="flex gap-4">
          <li>
            <NuxtLink to="/">Home</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/about">About</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/auth/login">Login</NuxtLink>
          </li>
        </ul>
      </nav>
    </header>
  </div>
  <div class="container mx-auto p-4">
    <slot></slot>
  </div>
</template>

<style scoped>

</style>
