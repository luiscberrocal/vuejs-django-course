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
  <div class="container mx-auto max-w-2xl">
    <header class="flex justify-between items-start md:items-center mt-5">
      <div class="flex items-center md:space-x-12">
        <MyHeader></MyHeader>
        <Menu/>
      </div>
      <ClientOnly>
        <ColorModeSelector/>
      </ClientOnly>
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

body {
  @apply bg-white dark:bg-gray-900 text-gray-700 dark:text-gray-300
}

</style>
