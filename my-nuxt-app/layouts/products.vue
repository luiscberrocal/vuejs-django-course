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
        <NuxtLink to="/products">Nuxt Dojo Merch</NuxtLink>
      </nav>
    </header>
  </div>
  <div>
    <slot></slot>
  </div>
  <footer>
    <nav>
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
  </footer>
</template>

<style scoped>

</style>
