<script lang="ts" setup>
useHead({
  titleTemplate: "%s - Luis C. Berrocal",
  link: [
    {
      rel: 'preconnect',
      href: 'https://fonts.googleapis.com'
    },
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Roboto&display=swap',
      crossorigin: ''
    }
  ]
})
</script>

<template>
  <div class="container mx-auto max-w-2xl mt-5">
    <header class="flex justify-between items-center">
      <NuxtLink to="/" class="text-xl">Luis C. Berrocal</NuxtLink>
      <Menu/>
    </header>

    <main class="p2 mt-10">
      <slot></slot>
    </main>


  </div>
</template>

<style>
body {
  font-family: 'Roboto';
}

</style>
