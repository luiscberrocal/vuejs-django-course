<script lang="ts" setup>

</script>

<template>
  <div class="container mx-auto max-w-2xl">
    <header class="flex justify-between">
      <NuxtLink to="/" class="text-xl">Luis C. Berrocal</NuxtLink>
      <nav>
        <ul class="flex">
          <li>
            <NuxtLink to="/">Home</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/about">About</NuxtLink>
          </li>
        </ul>
      </nav>

    </header>

    <slot></slot>

  </div>
</template>

<style scoped>

</style>
