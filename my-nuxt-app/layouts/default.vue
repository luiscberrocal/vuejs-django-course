<script lang="ts">
export default {
  props: [],
  data() {
    return {};
  },
  methods: {},
  computed: {}
}
</script>

<template>
  <div>
    <header class="shadow-sm bg-white">
      <nav class="container mx-auto p-4 flex justify-between">
        <NuxtLink to="/" class="font-bold">Nuxt Dojo</NuxtLink>
        <ul class="flex gap-4">
          <li>
            <NuxtLink to="/">Home</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/about">About</NuxtLink>
          </li>
          <li class="btn">
            <NuxtLink to="/products">Products</NuxtLink>
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
