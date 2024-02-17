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
    <header>
      <nav>
        <NuxtLink to="/">Nuxt Dojo</NuxtLink>
        <ul>
          <li>
            <NuxtLink to="/">Home</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/about">About</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/products">Products</NuxtLink>
          </li>
        </ul>
      </nav>
    </header>
  </div>
  <div>
    <slot></slot>
  </div>
</template>

<style scoped>

</style>
